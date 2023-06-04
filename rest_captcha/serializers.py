from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.core.cache import caches
from .settings import api_settings
from . import utils

cache = caches[api_settings.CAPTCHA_CACHE]


class RestCaptchaSerializer(serializers.Serializer):
    captcha_key = serializers.CharField(max_length=64)
    captcha_value = serializers.CharField(max_length=8, trim_whitespace=True)

    def validate(self, data):
        super(RestCaptchaSerializer, self).validate(data)
        cache_key = utils.get_cache_key(data['captcha_key'])

        if data['captcha_key'] in api_settings.MASTER_CAPTCHA:
            real_value = api_settings.MASTER_CAPTCHA[data['captcha_key']]
        else:
            real_value = cache.get(cache_key)

        if real_value is None:
            raise serializers.ValidationError(
                 _('Invalid or expired captcha key'))

        cache.delete(cache_key)
        if data['captcha_value'].upper() != real_value.upper():
            raise serializers.ValidationError(_('Invalid captcha value'))

        del data['captcha_key']
        del data['captcha_value']
        return data
