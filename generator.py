import pyqrcode
import uuid
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

rate_size = 0.35
markers = {
    'markers/pattern-marker-LERO.png': 'lerobot',
}
season = 1
number_of_chocolates_init = 1
number_of_chocolates_end = 602

animations = [ 'dancing_lb', 'death_lb', 'jump_lb', 'no_lb',
              'nopunch_lb', 'running_lb', 'thumbsup_lb', 'yes_lb']


def randomAnimation():
    return random.choice(animations)
def fillZero(v, max):
    sizeV= len(str(v))
    sizeMax= len(str(max))
    sizeZero = sizeMax - sizeV
    zeroText = ''
    for z in range(sizeZero):
        zeroText += '0'

    return '{}{}'.format(zeroText, v)

for marker in markers:
    for i in range(number_of_chocolates_init, number_of_chocolates_end):
        id_marker = '{season}-{index}-{glb}-{animation}-{uuid}'.format(season=season, index=i, glb=markers[marker],
                                                                       animation=randomAnimation(), uuid=uuid.uuid4().hex)
        print("generating marker {}".format(id_marker))
        qr = pyqrcode.QRCode(id_marker)
        qr.png('qr.png', scale=50, module_color=(0, 0, 0, 255))
        im = Image.open('qr.png')
        im = im.convert("RGBA")
        width = im.size[0]
        marker_width = int(width * rate_size)
        left = int((width-marker_width) * 0.5)
        upper = int((width-marker_width) * 0.5)
        logo = Image.open(marker)
        box = (left, upper, left + marker_width, upper + marker_width)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region, box)

        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("font.ttf", 150)
        draw.text((850, 2270),'AngulAR{}{}'.format(season, fillZero(i, number_of_chocolates_end)), (0, 0, 0), font=font)

        im.save('qrs/ar_{}_{}.png'.format(season, i))

