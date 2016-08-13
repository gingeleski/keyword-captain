import cv2
from PIL import Image
import PIL.ImageGrab
#import pytesseract

def takeScreenshot():
    """
    Capture a screenshot of the entire screen

    Returns:
        (Image)
    """

    return PIL.ImageGrab.grab()

image = takeScreenshot()
image.save("out.png")

img = cv2.imread("out.png")
