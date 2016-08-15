import cv2
from PIL import Image
import PIL.ImageGrab
#import pytesseract

class ScreenInterpreter(object):
    def __init__(self):
        """
        Static class, constructor doesn't really
        do anything.
        """
        pass

    def takeScreenshot(self):
        """
        Capture a screenshot of the entire screen

        Returns:
            (Image)
        """

        return PIL.ImageGrab.grab()

class ScrabbleBoggleInterpreter(ScreenInterpreter):
    def __init__(self):
        ScreenInterpreter.__init__(self)

    def locateBoard(self):
        pass

si = ScreenInterpreter()
image = si.takeScreenshot()
image.save("out.png")

img = cv2.imread("out.png")
