"""
Django settings for cove project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import environ
import os
import warnings

import raven

from django.utils.crypto import get_random_string

COVE_CONFIG = {
    'app_name': 'test',
    'app_base_template': 'base.html',
    'input_methods': ['upload', 'url', 'text'],
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'
secret_key = get_random_string(50, chars)
if 'SECRET_KEY' not in os.environ:
    warnings.warn('SECRET_KEY should be added to Environment Variables. Random key will be used instead.')

env = environ.Env(  # set default values and casting
    SENTRY_DSN=(str, ''),
    DEBUG=(bool, True),
    PIWIK_URL=(str, ''),
    PIWIK_SITE_ID=(str, ''),
    PIWIK_DIMENSION_MAP=(dict, {}),
    GOOGLE_ANALYTICS_ID=(str, ''),
    HOTJAR_ID=(str, ''),
    HOTJAR_SV=(str, ''),
    HOTJAR_DATE_INFO=(str, ''),
    ALLOWED_HOSTS=(list, []),
    SECRET_KEY=(str, secret_key),
    DB_NAME=(str, os.path.join(BASE_DIR, 'db.sqlite3')),
    DEBUG_TOOLBAR=(bool, False),
    # SCHEMA_URL_360=(str, 'https://raw.githubusercontent.com/ThreeSixtyGiving/standard/master/schema/'),
)

PIWIK = {
    'url': env('PIWIK_URL'),
    'site_id': env('PIWIK_SITE_ID'),
    'dimension_map': env('PIWIK_DIMENSION_MAP'),
}

GOOGLE_ANALYTICS_ID = env('GOOGLE_ANALYTICS_ID')

HOTJAR = {
    'id': env('HOTJAR_ID'),
    'sv': env('HOTJAR_SV'),
    'date_info': env('HOTJAR_DATE_INFO'),
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEALER_TYPE = 'git'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

if env('SENTRY_DSN'):
    RAVEN_CONFIG = {
        'dsn': env('SENTRY_DSN'),
        'release': raven.fetch_git_sha(os.path.join(os.path.dirname(__file__), '..')),
    }


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'cove',
    'cove.input',
)

if env('SENTRY_DSN'):
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

if env('DEBUG_TOOLBAR'):
    INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'dealer.contrib.django.Middleware',
    'cove.middleware.CoveConfigCurrentApp',
)

ROOT_URLCONF = 'cove.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cove.context_processors.analytics',
                'cove.context_processors.input_methods'
            ],
        },
    },
]

WSGI_APPLICATION = ''


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env('DB_NAME'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'cove', 'locale'),
)


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        '': {
            'level': 'WARNING',
            'handlers': ['console', 'sentry'],
        },
    },
}
