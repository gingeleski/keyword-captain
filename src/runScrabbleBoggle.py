# Runner for Scrabble Boggle

# Basically have the board fully visible, run this from
# a window that doesn't interfere, and go to town

# Scrabble Boggle @ worldwinner.com

from GameController import *

sbc = ScrabbleBoggleController()
sbc.captureAndSolve4Letter()
sbc.playSolutions4Letter()