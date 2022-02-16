from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters
import textwrap

img = Image.open(fp='images/input/img.png', mode='r')
logo = Image.open('images/input/logo/programming/strack.jpg')
logo = logo.resize((550, 550))
img.paste(logo, (170, 270), logo)

img.show()