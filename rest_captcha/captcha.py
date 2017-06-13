import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from .settings import api_settings as settings
from . import utils

try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

FONT = ImageFont.truetype(
    settings.CAPTCHA_FONT_PATH, settings.CAPTCHA_FONT_SIZE)


def filter_default(image):
    return utils.filter_smooth(image, ImageFilter.SMOOTH)


def noise_default(image, draw):
    draw = utils.noise_dots(draw, image, settings.CAPTCHA_FOREGROUND_COLOR)
    draw = utils.noise_arcs(draw, image, settings.CAPTCHA_FOREGROUND_COLOR)


def getsize(font, text):
    if hasattr(font, 'getoffset'):
        return tuple(
            [x + y for x, y in zip(font.getsize(text), font.getoffset(text))])
    else:
        return font.getsize(text)


def makeimg(size):
    if settings.CAPTCHA_BACKGROUND_COLOR == "transparent":
        image = Image.new('RGBA', size)
    else:
        image = Image.new('RGB', size, settings.CAPTCHA_BACKGROUND_COLOR)
    return image


def generate_image(word):
    font = FONT
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
            angle = random.randrange(*settings.CAPTCHA_LETTER_ROTATION)
            charimage = charimage.rotate(
                angle, expand=0, resample=Image.BICUBIC)

        charimage = charimage.crop(charimage.getbbox())
        maskimage = Image.new('L', size)

        xpos2 = xpos + charimage.size[0]
        from_top2 = from_top + charimage.size[1]
        maskimage.paste(charimage, (xpos, from_top, xpos2, from_top2))
        size = maskimage.size
        image = Image.composite(fgimage, image, maskimage)
        xpos = xpos + 2 + charimage.size[0]

    if settings.CAPTCHA_IMAGE_SIZE:
        # centering captcha on the image
        tmpimg = makeimg(size)
        xpos2 = int((size[0] - xpos) / 2)
        from_top2 = int((size[1] - charimage.size[1]) / 2 - from_top)
        tmpimg.paste(image, (xpos2, from_top2))
        image = tmpimg.crop((0, 0, size[0], size[1]))
    else:
        image = image.crop((0, 0, xpos + 1, size[1]))

    draw = ImageDraw.Draw(image)

    settings.FILTER_FUNCTION(image)
    settings.NOISE_FUNCTION(image, draw)

    out = StringIO()
    image.save(out, 'PNG')
    content = out.getvalue()
    out.seek(0)
    out.close()

    return content
