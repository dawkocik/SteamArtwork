from PIL import Image, ImageDraw, ImageOps
from psd_tools import PSDImage

# left 0-452
# right 460-549

six = Image.open(input("Image location:"), mode='r')
artwork = ImageOps.fit(six, (549, 452), Image.ANTIALIAS)
draw = ImageDraw.Draw(artwork)

draw.rectangle((452, 0, 459, 452), fill=(0, 0, 0, 0))

psd = PSDImage.frompil(artwork, 0)
psd.save("siema.psd")