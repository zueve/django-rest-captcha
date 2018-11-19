# Django rest captcha

Lightweight version of django-simple-captcha for work with django-rest-framework.


## Features
- speed: used `cache` instead database
- safety: union methods for generate key and image. (You can't generate many images for one key)
- easy: only one extended rest api (for generate, refresh image).


## Install
```
> pip install django-rest-captcha
```

### Add to your settings.py

Add to installed apps
```
INSTALLED_APPS = (
    ...
    'rest_captcha',
)
```

Set rest_captcha settings (if you want), see defaults:
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

We recommended  use redis or memcache. And LocMemCache for local tests with bigger value of MAX_ENTRIES:
```
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'rest-captcha',
        'MAX_ENTRIES': 10000,
    }
}
```

### Add hooks to your app router (urls.py)
```
urlpatterns = [
    ...
    url(r'api/captcha/', include('rest_captcha.urls')),
]
```

## Usage
Add `RestCaptchaSerializer` to your protected request validator:
```
from rest_captcha serializer import RestCaptchaSerializer
class HumanOnlySerializer(RestCaptchaSerializer):
    pass
```
This code add to your serializer two required fields (captcha_key, captcha_value):


For provide this field client should generate key:
```
> curl -X POST http:localhost:8000/api/captcha/ | python -m json.tool
{
    'image_type': 'image/png',
    'image_decode': 'base64',
    'captcha_key': 'de67e7f3-72d9-42d8-9677-ea381610363d',
    'captcha_key': '... image encoded in base64'
}
```

Decode and understand world on image and make request to protected view. If your have mistake - your should re generate your image.
