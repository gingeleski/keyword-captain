from Board import Board
import os
from PIL import Image
import PIL.ImageGrab
import pyautogui as pag
from Values import ScrabbleValues

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
    game_area_top_left = os.path.abspath("../img/scrabble_boggle/game_top-left.png")
    game_area_bottom_right = os.path.abspath("../img/scrabble_boggle/game_bottom-right.png")

    game_area_top_left_x = -1
    game_area_top_left_y = -1
    game_area_bottom_right_x = -1
    game_area_bottom_right_y = -1
    
    def __init__(self):
        ScreenInterpreter.__init__(self)

    def isGameAreaKnown(self):
        if self.game_area_top_left_x == -1:
            return False
        elif self.game_area_top_left_y == -1:
            return False
        elif self.game_area_bottom_right_x == -1:
            return False
        elif self.game_area_bottom_right_y == -1:
            return False
        return True

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

    def isolate4LetterBoard(self, img=None):
        """
        Given an image of the screen, returns a cropped image of just
        the letter board
        """
        top_x = self.game_area_top_left_x + 263
        top_y = self.game_area_top_left_y + 81
        bottom_x = self.game_area_bottom_right_x - 107
        bottom_y = self.game_area_bottom_right_y - 78

        if img is None:
            current_screen = pag.screenshot()
            return current_screen.crop((top_x, top_y, bottom_x, bottom_y))
        else:
            return img.crop((top_x, top_y, bottom_x, bottom_y))

    def interpret4LetterBoard(self, img):
        brd = Board(4)

        letters_file_root = "../img/scrabble_boggle/letters/"
        letters_file_list = os.listdir(letters_file_root)

        cells_identified = 0

        for letter_img in letters_file_list:
            this_letter = letters_file_root + letter_img
            results = pag.locateAll(this_letter, img)
            for match in results:
                cells_identified += 1
                letter = str(letter_img[:-4]).lower()
                value = ScrabbleValues[letter]
                if match[0] < 93 and match[1] < 93:
                    brd.board[0][0].set_letters(letter)
                    brd.board[0][0].set_value(value)
                elif match[0] >= 93 and match[0] < 194 and match[1] < 93:
                    brd.board[0][1].set_letters(letter)
                    brd.board[0][1].set_value(value)
                elif match[0] >= 194 and match[0] < 292 and match[1] < 93:
                    brd.board[0][2].set_letters(letter)
                    brd.board[0][2].set_value(value)
                elif match[0] >= 292 and match[1] < 93:
                    brd.board[0][3].set_letters(letter)
                    brd.board[0][3].set_value(value)
                elif match[0] < 93 and match[1] >= 93 and match[1] < 193:
                    brd.board[1][0].set_letters(letter)
                    brd.board[1][0].set_value(value)
                elif match[0] >= 93 and match[0] < 194 and match[1] >= 93 and match[1] < 193:
                    brd.board[1][1].set_letters(letter)
                    brd.board[1][1].set_value(value)
                elif match[0] >= 194 and match[0] < 292 and match[1] >= 93 and match[1] < 193:
                    brd.board[1][2].set_letters(letter)
                    brd.board[1][2].set_value(value)
                elif match[0] >= 292 and match[1] >= 93 and match[1] < 193:
                    brd.board[1][3].set_letters(letter)
                    brd.board[1][3].set_value(value)
                elif match[0] < 93 and match[1] >= 193 and match[1] < 292:
                    brd.board[2][0].set_letters(letter)
                    brd.board[2][0].set_value(value)
                elif match[0] >= 93 and match[0] < 194 and match[1] >= 193 and match[1] < 292:
                    brd.board[2][1].set_letters(letter)
                    brd.board[2][1].set_value(value)
                elif match[0] >= 194 and match[0] < 292 and match[1] >= 193 and match[1] < 292:
                    brd.board[2][2].set_letters(letter)
                    brd.board[2][2].set_value(value)
                elif match[0] >= 292 and match[1] >= 193 and match[1] < 292:
                    brd.board[2][3].set_letters(letter)
                    brd.board[2][3].set_value(value)
                elif match[0] < 93 and match[1] >= 292:
                    brd.board[3][0].set_letters(letter)
                    brd.board[3][0].set_value(value)
                elif match[0] >= 93 and match[0] < 194 and match[1] >= 292:
                    brd.board[3][1].set_letters(letter)
                    brd.board[3][1].set_value(value)
                elif match[0] >= 194 and match[0] < 292 and match[1] >= 292:
                    brd.board[3][2].set_letters(letter)
                    brd.board[3][2].set_value(value)
                elif match[0] >= 292 and match[1] >= 292:
                    brd.board[3][3].set_letters(letter)
                    brd.board[3][3].set_value(value)
            if cells_identified == 16:
                break

        return brd