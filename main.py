from copy import copy
from Board import Board
from FileManager import loadWordList

# Warning - hacky testing below
wordlist = loadWordList("words.txt")
brd = Board()
print(brd.board[0][0].value)