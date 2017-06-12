import random


def random_char_challenge(length):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(length):
        ret += random.choice(chars)
    return ret.upper()