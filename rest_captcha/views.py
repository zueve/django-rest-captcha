import uuid
import base64
from rest_framework import views, response
from django.core.cache import caches
from .settings import api_settings
from . import utils
from . import captcha

cache = caches[api_settings.CAPTCHA_CACHE]


class RestCapthaView(views.APIView):
    def post(self, request):
        key = str(uuid.uuid4())
        value = utils.random_char_challenge(api_settings.CAPTCHA_LENGTH)

        cache.set(key, value, api_settings.CAPTCHA_TIMEOUT)

        # generate image
        image_bytes = captcha.generate_image(value)
        image_b64 = base64.b64encode(image_bytes)

        data = dict(
            captcha_key=key,
            captcha_image=image_b64,
            content_type='image/png'
        )
        return response.Response(data)
