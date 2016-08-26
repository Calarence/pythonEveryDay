#!/usr/bin/env python
# encoding: utf-8
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


text = u"+1"

im = Image.open('./image.jpg')

dr = ImageDraw.Draw(im)
#font = ImageFont.truetype('arial.ttf', 34)
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 25)
dr.text((im.size[0]*0.85, im.size[1]*0.05), text,font=font, fill="#ff0000")

im.show()
im.save('result.jpg')
