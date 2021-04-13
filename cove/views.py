import functools
import logging
from datetime import timedelta

from django.db.models.aggregates import Count
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError

from cove.input.models import SuppliedData
from flattentool.json_input import BadlyFormedJSONError
from libcove.lib.exceptions import CoveInputDataError, UnrecognisedFileType
from libcove.lib.tools import get_file_type as _get_file_type

logger = logging.getLogger(__name__)


def cove_web_input_error(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)
        except BadlyFormedJSONError as err:
            context={
                "sub_title": _("Sorry, we can't process that data"),
                "link": "index",
                "link_text": _("Try Again"),
                "msg": _(
                    "We think you tried to upload a JSON file, but it is not well formed JSON.\n\nError message: {}".format(
                        err
                    )
                ),
            }
        except UnrecognisedFileType:
            context = {
                "sub_title": _("Sorry, we can't process that data"),
                "link": "index",
                "link_text": _("Try Again"),
                "msg": _(
                    "We did not recognise the file type.\n\nWe can only process json, csv, ods and xlsx files."
                ),
            }
        except CoveInputDataError as err:
            if hasattr(err, "wrapped_err"):
                context = {
                        "sub_title": _("Sorry, we can't process that data"),
                        "link": "index",
                        "link_text": _("Try Again"),
                        "msg": _(
                            "We think you tried to supply a spreadsheet, but we failed to convert it."
                            "\n\nError message: {}"
                        ).format(repr(err.wrapped_err)),
                }
            else:
                context = err.context
        return render(request, 'error.html', context=context)
    return wrapper


def get_file_name(file_name):
    if file_name is not None and '/' in file_name:
        file_name = file_name.split('/')[-1]
    return file_name


def explore_data_context(request, pk, get_file_type=None):
    if get_file_type is None:
        get_file_type = _get_file_type

    try:
        data = SuppliedData.objects.get(pk=pk)
    except (SuppliedData.DoesNotExist, ValidationError):  # Catches primary key does not exist and badly formed UUID
        return {}, None, render(request, 'error.html', {
            'sub_title': _('Sorry, the page you are looking for is not available'),
            'link': 'index',
            'link_text': _('Go to Home page'),
            'msg': _("We don't seem to be able to find the data you requested.")
            }, status=404)

    try:
        file_name = data.original_file.file.name
        if file_name.endswith('validation_errors-3.json'):
            raise PermissionError('You are not allowed to upload a file with this name.')
    except FileNotFoundError:
        return {}, None, render(request, 'error.html', {
            'sub_title': _('Sorry, the page you are looking for is not available'),
            'link': 'index',
            'link_text': _('Go to Home page'),
            'msg': _('The data you were hoping to explore no longer exists.\n\nThis is because all '
                     'data supplied to this website is automatically deleted after 7 days, and therefore '
                     'the analysis of that data is no longer available.')
        }, status=404)

    file_type = get_file_type(data.original_file)
    context = {
        'original_file': {
            'url': data.original_file.url,
            'size': data.original_file.size,
            'path': data.original_file.path,
        },
        'file_type': file_type,
        'file_name': get_file_name(file_name),
        'data_uuid': pk,
        'current_url': request.build_absolute_uri(),
        'source_url': data.source_url,
        'form_name': data.form_name,
        'created_datetime': data.created.strftime('%A, %d %B %Y %I:%M%p %Z'),
        'created_date': data.created.strftime('%A, %d %B %Y'),
        'created_time': data.created.strftime('%I:%M%p %Z'),
    }

    return (context, data, None)


def stats(request):
    query = SuppliedData.objects.filter(current_app=request.current_app)
    by_form = query.values('form_name').annotate(Count('id'))
    return render(request, 'stats.html', {
        'uploaded': query.count(),
        'total_by_form': {x['form_name']: x['id__count'] for x in by_form},
        'upload_by_time_by_form': [(
            num_days,
            query.filter(created__gt=timezone.now() - timedelta(days=num_days)).count(),
            {x['form_name']: x['id__count'] for x in by_form.filter(created__gt=timezone.now() - timedelta(days=num_days))}
        ) for num_days in [1, 7, 30]],
    })
