from pytesseract import image_to_string
from PIL import Image
from PIL import ImageFilter
import gsimage
import os


def runOCR(image):
    im = image.filter(ImageFilter.UnsharpMask(radius=1, percent=100, threshold=5))
    im.show()
    print image_to_string(im, lang='jpn', config='-psm 5')
