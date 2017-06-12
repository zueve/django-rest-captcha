import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from .settings import api_settings as settings
from . import utils

try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO


def filter_default(image):
    return utils.filter_smooth(image, ImageFilter.SMOOTH)


def random_char_challenge():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ret = ''
    for i in range(settings.CAPTCHA_LENGTH):
        ret += random.choice(chars)
    return ret.upper()


def noise_dots(draw, image):
    size = image.size
    for p in range(int(size[0] * size[1] * 0.1)):
        draw.point((random.randint(0, size[0]), random.randint(0, size[1])), fill=settings.CAPTCHA_FOREGROUND_COLOR)
    return draw


def noise_arcs(draw, image):
    size = image.size
    draw.arc([-20, -20, size[0], 20], 0, 295, fill=settings.CAPTCHA_FOREGROUND_COLOR)
    draw.line([-20, 20, size[0] + 20, size[1] - 20], fill=settings.CAPTCHA_FOREGROUND_COLOR)
    draw.line([-20, 0, size[0] + 20, size[1]], fill=settings.CAPTCHA_FOREGROUND_COLOR)
    return draw


def getsize(font, text):
    if hasattr(font, 'getoffset'):
        return tuple([x + y for x, y in zip(font.getsize(text), font.getoffset(text))])
    else:
        return font.getsize(text)


def makeimg(size):
    if settings.CAPTCHA_BACKGROUND_COLOR == "transparent":
        image = Image.new('RGBA', size)
    else:
        image = Image.new('RGB', size, settings.CAPTCHA_BACKGROUND_COLOR)
    return image


def generate_image(word, scale=1):
    fontpath = settings.CAPTCHA_FONT_PATH
    font = ImageFont.truetype(fontpath, settings.CAPTCHA_FONT_SIZE * scale)
    size = settings.CAPTCHA_IMAGE_SIZE

    xpos = 2
    from_top = 4

    image = makeimg(size)

    for char in word:
        fgimage = Image.new('RGB', size, settings.CAPTCHA_FOREGROUND_COLOR)
        charimage = Image.new('L', getsize(font, ' %s ' % char), '#000000')
        chardraw = ImageDraw.Draw(charimage)
        chardraw.text((0, 0), ' %s ' % char, font=font, fill='#ffffff')
        if settings.CAPTCHA_LETTER_ROTATION:
            charimage = charimage.rotate(random.randrange(*settings.CAPTCHA_LETTER_ROTATION), expand=0, resample=Image.BICUBIC)

        charimage = charimage.crop(charimage.getbbox())
        maskimage = Image.new('L', size)

        maskimage.paste(charimage, (xpos, from_top, xpos + charimage.size[0], from_top + charimage.size[1]))
        size = maskimage.size
        image = Image.composite(fgimage, image, maskimage)
        xpos = xpos + 2 + charimage.size[0]

    if settings.CAPTCHA_IMAGE_SIZE:
        # centering captcha on the image
        tmpimg = makeimg(size)
        tmpimg.paste(image, (int((size[0] - xpos) / 2), int((size[1] - charimage.size[1]) / 2 - from_top)))
        image = tmpimg.crop((0, 0, size[0], size[1]))
    else:
        image = image.crop((0, 0, xpos + 1, size[1]))

    draw = ImageDraw.Draw(image)

    image = settings.FILTER_FUNCTION(image)
    # for f in settings.noise_functions():
    #     draw = f(draw, image)
    # for f in settings.filter_functions():
    image.save('captcha.png', 'PNG')
    out = StringIO()
    image.save(out, 'PNG')
    content = out.getvalue()
    out.seek(0)
    out.close()

    return content
