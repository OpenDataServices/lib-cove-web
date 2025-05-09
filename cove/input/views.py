import json
import requests

from django import forms
from django.conf import settings
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

from cove.input.models import SuppliedData
from django.views.decorators.csrf import csrf_protect


class UploadForm(forms.ModelForm):
    class Meta:
        model = SuppliedData
        fields = ['original_file']
        labels = {
            'original_file': _('Upload a file (.json, .csv, .xlsx, .ods)')
        }


class UrlForm(forms.ModelForm):
    class Meta:
        model = SuppliedData
        fields = ['source_url']
        labels = {
            'source_url': _('Supply a URL')
        }


class TextForm(forms.Form):
    paste = forms.CharField(label=_('Paste (JSON only)'), widget=forms.Textarea)


default_form_classes = {
    'upload_form': UploadForm,
    'url_form': UrlForm,
    'text_form': TextForm,
}


@csrf_protect
def data_input(request, form_classes=default_form_classes, text_file_name='test.json'):
    forms = {form_name: form_class() for form_name, form_class in form_classes.items()}
    request_data = None
    if "source_url" in request.GET and settings.COVE_CONFIG.get("allow_direct_web_fetch", False):
        request_data = request.GET
    if request.POST:
        request_data = request.POST
    if request_data:
        if 'source_url' in request_data:
            form_name = 'url_form'
        elif 'paste' in request_data:
            form_name = 'text_form'
        else:
            form_name = 'upload_form'
        form = form_classes[form_name](request_data, request.FILES)
        forms[form_name] = form
        if form.is_valid():
            if form_name == 'text_form':
                data = SuppliedData()
            else:
                data = form.save(commit=False)
            data.current_app = request.current_app
            data.form_name = form_name

            try:
                # We don't want to store large chunks of pasted data that might be in the request data.
                if not "paste" in request_data:
                    data.parameters = json.dumps(request_data)
            except TypeError:
                pass

            data.save()
            if form_name == 'url_form':
                try:
                    data.download()
                except requests.exceptions.InvalidURL as err:
                    return render(request, 'error.html', context={
                        'sub_title': _("That URL is invalid"),
                        'link': 'index',
                        'link_text': _('Try Again'),
                        'msg': str(err)
                    })
                except requests.Timeout as err:
                    return render(request, 'error.html', context={
                        'sub_title': _(
                            "The request timed out after %(timeout)s seconds"
                        ) % getattr(settings, "REQUESTS_TIMEOUT", "indefinite"),
                        'link': 'index',
                        'link_text': _('Try Again'),
                        'msg': str(err)
                    })
                except requests.ConnectionError as err:
                    return render(request, 'error.html', context={
                        'sub_title': _("Sorry we got a ConnectionError whilst trying to download that file"),
                        'link': 'index',
                        'link_text': _('Try Again'),
                        'support_email': settings.COVE_CONFIG.get('support_email'),
                        'msg': str(err) + '\n\n' + str(_('Common reasons for this error include supplying a local '
                                 'development url that our servers can\'t access, or misconfigured SSL certificates.'))
                    })
                except requests.HTTPError as err:
                    return render(request, 'error.html', context={
                        'sub_title': _("Sorry we got a HTTP Error whilst trying to download that file"),
                        'link': 'index',
                        'link_text': _('Try Again'),
                        'support_email': settings.COVE_CONFIG.get('support_email'),
                        'msg': str(err) + '\n\n' + str(_('If you can access the file through a browser then the problem '
                                 'may be related to permissions, or you may be blocking certain user agents.'))
                    })
            elif form_name == 'text_form':
                data.original_file.save(text_file_name, ContentFile(form['paste'].value()))
            return redirect(data.get_absolute_url())

    return render(request, settings.COVE_CONFIG.get('input_template', 'input.html'), {'forms': forms})
