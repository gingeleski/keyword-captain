from PIL import Image
import PIL.ImageGrab

def takeScreenshot():
    """
    Capture a screenshot of the entire screen

    Returns:
        (Image)
    """

    return PIL.ImageGrab.grab(box)
