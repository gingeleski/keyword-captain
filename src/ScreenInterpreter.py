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

#print(pytesseract.image_to_string(takeScreenshot()))
