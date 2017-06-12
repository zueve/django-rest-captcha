# Django rest capthca

This is lightweight version of django-simple-captcha for work with
django-rest-framework.


## Features
- speed: use cache insted database
- safety: union methods for generate key and image. (You can't generate many images for one key)
- easy: only one rest api (for generate, refresh image).


## Install
```
> pip install django-rest-captcha
```

## Add to project

Add to installed apps
```
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```

Set rest_captcha serrings (if you want):
```
REST_CAPTCHA = {
    'CAPTCHA_CACHE': 'default',
    'CAPTCHA_TIMEOUT': 300,  # 5 minuts
    'CAPTCHA_LENGTH': 4,
    'CAPTCHA_FONT_SIZE': 22,
    'CAPTCHA_IMAGE_SIZE': (90, 40),
    'CAPTCHA_LETTER_ROTATION': (-35, 35),
    'CAPTCHA_FOREGROUND_COLOR': '#001100',
    'CAPTCHA_BACKGROUND_COLOR': '#ffffff',
    'CAPTCHA_FONT_PATH': FONT_PATH,
    'CAPTCHA_CACHE_KEY': 'rest_captcha_{key}.{version}',
    'FILTER_FUNCTION': 'rest_captcha.captcha.filter_default',
    'NOISE_FUNCTION': 'rest_captcha.captcha.noise_default'
}
```

We recommendete use radis or lacal memory as cache with set parameter, with bigger value of MAX_ENTRIES:
```
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'rest-captcha',
        'MAX_ENTRIES': 10000,
    }
}
```
