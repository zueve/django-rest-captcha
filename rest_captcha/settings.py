from rest_framework.settings import APISettings
from django.conf import settings
import os


USER_SETTINGS = getattr(settings, 'REST_CAPTCHA', None)

FONT_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'fonts/Vera.ttf')

small_letters = 'abcdefghijklmnopqrstuvwxyz'
numeric_chars = '0123456789'
ALPHABET_CHOICES = {
    'capital_letters': small_letters.upper(),
    'small_letters': small_letters,
    'numeric': numeric_chars,
    'small_and_capital': small_letters + small_letters.upper(),
    'capital_and_numeric': small_letters.upper() + numeric_chars,
    'small_and_numeric': small_letters + numeric_chars,
    'all': small_letters + small_letters.upper() + numeric_chars
}

DEFAULTS = {
    'CAPTCHA_CACHE': 'default',
    'CAPTCHA_ALPHABET': 'capital_letters',
    'CAPTCHA_TIMEOUT': 300,  # 5 minutes
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
    'NOISE_FUNCTION': 'rest_captcha.captcha.noise_default',
    # for tests access: MASTER_CAPTCHA: {'secret_key: secret_value'}
    'MASTER_CAPTCHA': {}
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = ('FILTER_FUNCTION', 'NOISE_FUNCTION')

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)

assert api_settings.CAPTCHA_ALPHABET in ALPHABET_CHOICES, "`CAPTCHA_ALPHABET` is Invalid."
