import os
from PIL import Image
import PIL.ImageGrab
import pyautogui as pag

class ScreenInterpreter(object):
    def __init__(self):
        """
        Static class, constructor does nothing
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
    game_area_top_left = os.path.abspath("../resources/scrabble-boggle_img/game-area_top-left.png")
    game_area_bottom_right = os.path.abspath("../resources/scrabble-boggle_img/game-area_bottom-right.png")
    
    def __init__(self):
        ScreenInterpreter.__init__(self)

    def locateBoard(self, img):
        """
        Locates the game board on a given image

        Args:
            img (str) - image file path

        Returns:
            (Tuple) - top left x, top left y, bottom right x, bottom right y
        """
        top_left = pag.locate(self.game_area_top_left, img)
        bottom_right = pag.locate(self.game_area_bottom_right, img)

        if top_left is None or bottom_right is None:
            return None

        return top_left[0], top_left[1], bottom_right[0], bottom_right[1]

    def locateBoardOnScreen(self):
        """
        Locates the game board on current screen

        Returns:
            (Tuple) - top left x, top left y, bottom right x, bottom right y
        """
        top_left = pag.locateOnScreen(self.game_area_top_left)
        bottom_right = pag.locateOnScreen(self.game_area_bottom_right)

        if top_left is None or bottom_right is None:
            return None

        return top_left[0], top_left[1], bottom_right[0], bottom_right[1]