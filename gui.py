from Tkinter import *
from gsimage import *
import ocr
import pythoncom, pyHook
from pyHook.HookManager import HookConstants
trace = 0

root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes('-alpha', 0.5)


class CanvasEventsDemo:
#defines attributes of GUI
    def __init__(self, parent=None):
        canvas = Canvas(width=300, height=300, bg=None)
        canvas.pack(fill=BOTH, expand=YES)
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<ButtonRelease-1>', self.onEnd)
        canvas.bind('<B1-Motion>',     self.onGrow)
        self.canvas = canvas
        self.drawn  = None
        self.kinds = [canvas.create_rectangle]
        self.coords = []
# What to do when the mouse button is pressed
    def onStart(self, event):
        self.shape = self.canvas.create_rectangle
        self.start = event
        self.drawn = None
        (startx, starty) = self.start.x, self.start.y
        self.coords.append(startx)
        self.coords.append(starty)
        print (startx, starty)
# What to do as the mouse is in motion
    def onGrow(self, event):
        canvas = event.widget
        if self.drawn:
            canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y, width=5)
        if trace: print objectId
        self.drawn = objectId

#What to do when the mouse button is released
    def onEnd(self, event):
        (endx, endy) = event.x, event.y
        self.coords.append(endx)
        self.coords.append(endy)
        return self.coords, root.destroy()

def onKeyboardEvent(event):
    if ctrl_pressed:
        mainloop()
        img = GSImage(gui.coords)
        ocr.runOCR(img.image)
        quit()
        hm.disconnect()
if __name__ == '__main__':
    gui = CanvasEventsDemo()
    hm = pyHook.HookManager()
    hm.SubscribeKeyDown(onKeyboardEvent)
    hm.HookKeyboard()
    ctrl_pressed = hm.key_hook = "VK_CONTROL"
    pythoncom.PumpMessages()
