from PIL import Image, ImageDraw
from inky import InkyPHAT

display = InkyPHAT('red')
display.set_border(display.WHITE)

img = Image.open('resources/TWA-inky.png')
draw = ImageDraw.Draw(img)

display.set_image(img)
display.show()
