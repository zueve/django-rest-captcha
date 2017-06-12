import random


def random_char_challenge(length):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(length):
        ret += random.choice(chars)
    return ret.upper()


def filter_smooth(image, filter_code):
    return image.filter(filter_code)
