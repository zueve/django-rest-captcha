import random
from rest_captcha import VERSION
from .settings import api_settings

cache_template = api_settings.CAPTCHA_CACHE_KEY


def get_cache_key(captcha_key):
    cache_key = cache_template.format(key=captcha_key, version=VERSION.major)
    return cache_key


def random_char_challenge(length):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(length):
        ret += random.choice(chars)
    return ret.upper()


def filter_smooth(image, filter_code):
    return image.filter(filter_code)


def noise_dots(draw, image, fill):
    size = image.size
    for p in range(int(size[0] * size[1] * 0.1)):
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        draw.point((x, y), fill=fill)
    return draw


def noise_arcs(draw, image, fill):
    size = image.size
    draw.arc([-20, -20, size[0], 20], 0, 295, fill=fill)
    draw.line([-20, 20, size[0] + 20, size[1] - 20], fill=fill)
    draw.line([-20, 0, size[0] + 20, size[1]], fill=fill)
    return draw
