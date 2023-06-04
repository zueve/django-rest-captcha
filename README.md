# Django rest captcha

Lightweight version of `django-simple-captcha` for work with `django-rest-framework`.


## Features

- Speed: use `cache` instead of database
- Safety: union methods for generate key and image. (You can't generate many images for one key)
- Easy: only one rest api (for generate, refresh image).


## Usage
Add `RestCaptchaSerializer` to your protected request validator:
```
from rest_captcha.serializer import RestCaptchaSerializer
class HumanOnlyDataSerializer(RestCaptchaSerializer):
    pass
```
This code add to your serializer two required fields (captcha_key, captcha_value)


For provide this fields client(js code) should generate key:
```
> curl -X POST http:localhost:8000/api/captcha/ | python -m json.tool
{
    'image_type': 'image/png',
    'image_decode': 'base64',
    'captcha_key': 'de67e7f3-72d9-42d8-9677-ea381610363d',
    'captcha_image': '... image encoded in base64'
}
```
`captcha_value` - is base64 encoded PNG image, client should decode and show this image to human for validation and send letters from captcha to protected api.
If human have mistake - client should re generate your image.

**Note:** See also [trottling](https://www.django-rest-framework.org/api-guide/throttling/) for protect public api


## Install
```
> pip install django-rest-captcha
```

### Add to your settings.py
Add to installed apps:
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
    'CAPTCHA_ALPHABET': 'capital_letters',
    'CAPTCHA_TIMEOUT': 300,  # 5 minutes
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
##### CAPTCHA_ALPHABET
The key `CAPTCHA_ALPHABET` defines the characters that the captcha code will be created with. It can contain small or capital letters or numbers or a combination of them. The possible values are `capital_letters`, `small_letters`, `numeric`, `small_and_capital`, `capital_and_numeric`, `small_and_numeric` and `all`.


We recommend using redis or local memory as cache with set parameter, with bigger value of MAX_ENTRIES:
```
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'rest-captcha',
        'MAX_ENTRIES': 10000,
    }
}
```

### Add hooks to your app router (urls.py):
```
urlpatterns = [
    ...
    url(r'api/captcha/', include('rest_captcha.urls')),
]
```
