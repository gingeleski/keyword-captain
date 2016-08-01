from copy import copy
from Board import Board
from FileManager import loadWordTree
from Solver import solve, results_list

# Warning - hacky testing below

# This will only work on Unix...
word_tree = loadWordTree("/usr/share/dict/words")

brd = Board(4)

brd.board[0][0].set_letters("y")
brd.board[0][0].set_value(4)

brd.board[0][1].set_letters("v")
brd.board[0][1].set_value(4)

brd.board[0][2].set_letters("a")
brd.board[0][2].set_value(1)

brd.board[0][3].set_letters("g")
brd.board[0][3].set_value(2)

brd.board[1][0].set_letters("l")
brd.board[1][0].set_value(1)

brd.board[1][1].set_letters("w")
brd.board[1][1].set_value(4)

brd.board[1][2].set_letters("k")
brd.board[1][2].set_value(5)

brd.board[1][3].set_letters("a")
brd.board[1][3].set_value(1)

brd.board[2][0].set_letters("b")
brd.board[2][0].set_value(3)

brd.board[2][1].set_letters("o")
brd.board[2][1].set_value(1)

brd.board[2][2].set_letters("t")
brd.board[2][2].set_value(1)

brd.board[2][3].set_letters("e")
brd.board[2][3].set_value(1)

brd.board[3][0].set_letters("i")
brd.board[3][0].set_value(1)

brd.board[3][1].set_letters("p")
brd.board[3][1].set_value(3)

brd.board[3][2].set_letters("a")
brd.board[3][2].set_value(1)

brd.board[3][3].set_letters("u")
brd.board[3][3].set_value(1)

results = solve(word_tree, brd)
