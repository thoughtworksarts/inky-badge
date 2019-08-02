from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT

display = InkyPHAT('red')
display.set_border(display.WHITE)

name = 'Julien Deswaef'
logo = Image.open('resources/TWA-inky.png')
font = ImageFont.truetype('resources/OpenSans-Regular.ttf', 16)

canvas = Image.new('P', (display.WIDTH, display.HEIGHT))

draw = ImageDraw.Draw(canvas)

w, h = font.getsize(name)
x = (display.WIDTH / 2) - (w / 2)
y = display.HEIGHT  - (h+5)

canvas.paste(logo, (0, -10))
draw.rectangle(((0, y), (display.WIDTH, display.HEIGHT)), fill=display.RED)
draw.text((x, y), name, display.WHITE, font)

display.set_image(canvas)
display.show()
