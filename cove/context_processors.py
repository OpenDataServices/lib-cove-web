from django.conf import settings


def from_settings(request):
    context = {
        'input_methods': settings.COVE_CONFIG.get('input_methods', []),
        'app_verbose_name': settings.COVE_CONFIG.get('app_verbose_name', []),

        'piwik': settings.PIWIK,
        'google_analytics_id': settings.GOOGLE_ANALYTICS_ID,
    }
    return context
