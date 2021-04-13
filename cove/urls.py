from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from django.template import loader
from django.http import HttpResponseServerError

import cove.input.views
import cove.views


def handler500(request):
    """500 error handler which includes ``request`` in the context.
    """

    context = {
        'request': request,
    }
    context.update(settings.COVE_CONFIG)

    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(context))


def cause500(request):
    raise Exception


urlpatterns = [
    re_path(r'^$', cove.input.views.data_input, name='index'),
    re_path(r'^terms/$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    re_path(r'^stats/$', cove.views.stats, name='stats'),
    re_path(r'^test/500$', cause500),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^i18n/', include('django.conf.urls.i18n'))
]
