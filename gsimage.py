# <== include('examples/showgrabbox.py')==>
from PIL import ImageGrab
from pymouse import PyMouse
from ctypes import *
from PIL import Image


user32dll = windll.LoadLibrary("C:\Windows\System32\User32.dll")
print user32dll.SetProcessDPIAware(1)


class GSImage():
    def __init__(self, coords):
        self.coords = coords
        self.image = self.getGSImage()

    # Gets mouse coordinates and then assigns X/Y values for bounding box
    def mousepos(self):
        m = PyMouse()
        (mousex, mousey) = m.position()
        (startx, starty) = mousex - 100, mousey - 50
        (endx, endy) = mousex + 100, mousey + 50
        return [startx, starty, endx, endy]

    # Captures screen from bounding box coordinates
    def getGSImage(self):
        im = ImageGrab.grab(bbox=(self.coords))
        im = im.convert('L')
        return im
