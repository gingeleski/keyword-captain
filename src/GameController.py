from FileManager import loadWordList, loadWordTree
import pyautogui as pag
from ScreenInterpreter import ScrabbleBoggleInterpreter
from Solver import Solver
import time

class GameController(object):
    def __init__(self):
        """
        Static class, constructor doesn't really
        do anything.
        """
        pass

    def click(self, click_x=None, click_y=None):
        if click_x is None or click_y is None:
            pag.click()
        else:
            pag.click(x=click_x, y=click_y)

class ScrabbleBoggleController(GameController):
    sbi = ScrabbleBoggleInterpreter()
    solver = Solver()
    word_list = None
    word_tree = None
    
    def __init__(self):
        GameController.__init__(self)
        word_file = "../wordlists/words_scrabble.txt"
        self.word_list = loadWordList(word_file)
        self.word_tree = loadWordTree(word_file)

    def captureAndSolve4Letter(self):
        if self.sbi.isGameAreaKnown() == False:
            self.sbi.locateGameArea()
        brd_img = self.sbi.isolate4LetterBoard()
        current_brd = self.sbi.interpret4LetterBoard(brd_img)
        self.solver.solve(self.word_tree, self.word_list, current_brd)

    def playSolutions4Letter(self):
        x_offset = self.sbi.game_area_top_left_x
        y_offset = self.sbi.game_area_top_left_y
        for w in self.solver.results_list:
            x = 0
            y = 0
            print("Playing " + str(w).upper())
            for l in w.word:
                if l.get_coordinates() == (0,0):
                    x = x_offset + 307
                    y = y_offset + 125
                elif l.get_coordinates() == (0,1):
                    x = x_offset + 407
                    y = y_offset + 125
                elif l.get_coordinates() == (0,2):
                    x = x_offset + 507
                    y = y_offset + 125
                elif l.get_coordinates() == (0,3):
                    x = x_offset + 607
                    y = y_offset + 125
                elif l.get_coordinates() == (1,0):
                    x = x_offset + 307
                    y = y_offset + 225
                elif l.get_coordinates() == (1,1):
                    x = x_offset + 407
                    y = y_offset + 225
                elif l.get_coordinates() == (1,2):
                    x = x_offset + 507
                    y = y_offset + 225
                elif l.get_coordinates() == (1,3):
                    x = x_offset + 607
                    y = y_offset + 225
                elif l.get_coordinates() == (2,0):
                    x = x_offset + 307
                    y = y_offset + 325
                elif l.get_coordinates() == (2,1):
                    x = x_offset + 407
                    y = y_offset + 325
                elif l.get_coordinates() == (2,2):
                    x = x_offset + 507
                    y = y_offset + 325
                elif l.get_coordinates() == (2,3):
                    x = x_offset + 607
                    y = y_offset + 325
                elif l.get_coordinates() == (3,0):
                    x = x_offset + 307
                    y = y_offset + 425
                elif l.get_coordinates() == (3,1):
                    x = x_offset + 407
                    y = y_offset + 425
                elif l.get_coordinates() == (3,2):
                    x = x_offset + 507
                    y = y_offset + 425
                elif l.get_coordinates() == (3,3):
                    x = x_offset + 607
                    y = y_offset + 425
                else:
                    # Error case
                    x = x_offset
                    y = y_offset
                time.sleep(0.12)
                self.click(x,y)
            # Click the last letter again to submit
            self.click(x,y)

sbc = ScrabbleBoggleController()
sbc.captureAndSolve4Letter()
sbc.playSolutions4Letter()