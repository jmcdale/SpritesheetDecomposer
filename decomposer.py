import os

from PIL import Image


def isSolidExtrema(extrema):
    return extrema[0][0] == extrema[0][1] and \
           extrema[1][0] == extrema[1][1] and \
           extrema[2][0] == extrema[2][1] and \
           extrema[3][0] == extrema[3][1]


def isBlank(image):
    extrema = image.convert("RGBA").getextrema()
    return isSolidExtrema(extrema)


def decompose(input_path, output_path, width, height, margin, spacing):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    image = Image.open(input_path)
    img_width, img_height = image.size
    idx = 0
    for y in range(margin, img_height, height + spacing):
        for x in range(margin, img_width, width + spacing):
            box = (x, y, x + width, y + height)
            cropped = image.crop(box)
            if not isBlank(cropped):
                cropped.save(os.path.join(output_path, "IMG_%s.png" % idx))
                idx += 1


decompose("rogue_characters.png", "./output_characters", 16, 16, 0, 1)
