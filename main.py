from copy import copy
from Board import Board
from FileManager import loadWordList

# Warning - hacky testing below
#wordlist = loadWordList("words.txt")

brd = Board(4)

neighbors = brd.get_neighbors(brd.board[3][3])
for x in neighbors:
    print(x.get_coordinates())