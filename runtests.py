import sys
import os
from django.conf import settings
from django.core.management import call_command

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

settings.configure(
    INSTALLED_APPS=(
        'django.contrib.auth', 'django.contrib.contenttypes',
        'rest_framework', 'rest_captcha', ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:',
        }
    },
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'rest-captcha',
            'MAX_ENTRIES': 10000,
        }
    },
    REST_FRAMEWORK={
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication'],
        'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny']
    },
    ROOT_URLCONF='rest_captcha.urls',
    MIDDLEWARE_CLASSES=(),
)

if __name__ == "__main__":
    try:
        from django.apps import apps
    except ImportError:
        pass
    else:
        apps.populate(settings.INSTALLED_APPS)
    call_command('test', 'rest_captcha')
