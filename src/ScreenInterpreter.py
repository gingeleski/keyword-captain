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

    game_area_top_left_x = -1
    game_area_top_left_y = -1
    game_area_bottom_right_x = -1
    game_area_bottom_right_y = -1
    
    def __init__(self):
        ScreenInterpreter.__init__(self)

    def locateGameArea(self, img=None):
        """
        Locates the game area on a given image, or the current screen
        if no image path is passed

        Args:
            img (str) - optional, image file path

        Returns:
            (Tuple) - top left x, top left y, bottom right x, bottom right y
        """
        if img is None:
            top_left = pag.locateOnScreen(self.game_area_top_left)
            bottom_right = pag.locateOnScreen(self.game_area_bottom_right)
        else:
            top_left = pag.locate(self.game_area_top_left, img)
            bottom_right = pag.locate(self.game_area_bottom_right, img)

        if top_left is not None and bottom_right is not None:
            self.game_area_top_left_x = top_left[0]
            self.game_area_top_left_y = top_left[1]
            self.game_area_bottom_right_x = bottom_right[0] + bottom_right[2]
            self.game_area_bottom_right_y = bottom_right[1] + bottom_right[3]

    def isolateLetterBoard(self, img):
        """
        Given an image of the screen, returns a cropped image of just
        the letter board
        """
        top_x = self.game_area_top_left_x + 263
        top_y = self.game_area_top_left_y + 81
        bottom_x = self.game_area_bottom_right_x - 90
        bottom_y = self.game_area_bottom_right_y - 50

        return img.crop((top_x, top_y, bottom_x, bottom_y))

sbi = ScrabbleBoggleInterpreter()
the_path = os.path.abspath("../resources/scrabble-boggle_img/sample-fullscreen.png")
sbi.locateGameArea(the_path)

im = Image.open(the_path)
im_cropped = sbi.isolateLetterBoard(im)
im_cropped.show()