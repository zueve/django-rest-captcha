import uuid
import base64
from rest_framework import views, response
from django.core.cache import caches
from rest_captcha import VERSION
from .settings import api_settings
from . import utils
from . import captcha

cache = caches[api_settings.CAPTCHA_CACHE]
cache_template = api_settings.CAPTCHA_CACHE_KEY


class RestCapthaView(views.APIView):
    def post(self, request):
        key = str(uuid.uuid4())
        value = utils.random_char_challenge(api_settings.CAPTCHA_LENGTH)
        cache_key = cache_template.format(key=key, version=VERSION.major)
        cache.set(cache_key, value, api_settings.CAPTCHA_TIMEOUT)

        # generate image
        image_bytes = captcha.generate_image(value)
        image_b64 = base64.b64encode(image_bytes)

        data = {
            api_settings.CAPTCHA_KEY: key,
            api_settings.CAPTCHA_IMAGE: image_b64,
            'image_type': 'image/png',
            'image_decode': 'base64'
        }
        return response.Response(data)
