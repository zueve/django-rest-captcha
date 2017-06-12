from rest_framework.settings import APISettings
from django.conf import settings
import os


USER_SETTINGS = getattr(settings, 'REST_CAPTCHA', None)

FONT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'fonts/Vera.ttf')

DEFAULTS = {
    'CAPTCHA_CACHE': 'default',
    'CAPTCHA_TIMEOUT': 300,  # 5 minuts
    'CAPTCHA_CACHE_KEY': 'rest_captcha_{key}.{version}',
    'CAPTCHA_KEY': 'captcha_key',
    'CAPTCHA_IMAGE': 'captcha_image',
    'CAPTCHA_LENGTH': 4,
    'CAPTCHA_FONT_PATH': FONT_PATH,
    'CAPTCHA_FONT_SIZE': 22,
    'CAPTCHA_IMAGE_SIZE': (90, 40),
    'CAPTCHA_LETTER_ROTATION': (-35, 35),
    'CAPTCHA_FOREGROUND_COLOR': '#001100',
    'CAPTCHA_BACKGROUND_COLOR': '#ffffff',
    'FILTER_FUNCTION': 'rest_captcha.captcha.filter_default',
    'NOISE_FUNCTION': 'rest_captcha.captcha.noise_default'
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = ('FILTER_FUNCTION', 'NOISE_FUNCTION')

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
