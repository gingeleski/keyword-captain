import sys
sys.path.append('../src')

from Board import Board
from FileManager import loadWordTree, loadWordList
from Solver import Solver

def test():
    # Use Scrabble word set
    word_tree = loadWordTree("../wordlists/words_scrabble.txt")
    word_list = loadWordList("../wordlists/words_scrabble.txt")

    brd = Board(4)

    brd.board[0][0].set_letters("d")
    brd.board[0][0].set_value(2)

    brd.board[0][1].set_letters("l")
    brd.board[0][1].set_value(1)
    brd.board[0][1].set_multiplier("TL")

    brd.board[0][2].set_letters("e")
    brd.board[0][2].set_value(1)
    brd.board[0][2].set_multiplier("TL")

    brd.board[0][3].set_letters("m")
    brd.board[0][3].set_value(3)

    brd.board[1][0].set_letters("y")
    brd.board[1][0].set_value(4)

    brd.board[1][1].set_letters("e")
    brd.board[1][1].set_value(1)

    brd.board[1][2].set_letters("n")
    brd.board[1][2].set_value(1)

    brd.board[1][3].set_letters("w")
    brd.board[1][3].set_value(4)

    brd.board[2][0].set_letters("s")
    brd.board[2][0].set_value(1)
    brd.board[2][0].set_multiplier("TW")

    brd.board[2][1].set_letters("r")
    brd.board[2][1].set_value(1)
    brd.board[2][1].set_multiplier("DL")

    brd.board[2][2].set_letters("c")
    brd.board[2][2].set_value(3)

    brd.board[2][3].set_letters("a")
    brd.board[2][3].set_value(1)

    brd.board[3][0].set_letters("i")
    brd.board[3][0].set_value(1)

    brd.board[3][1].set_letters("a")
    brd.board[3][1].set_value(1)

    brd.board[3][2].set_letters("b")
    brd.board[3][2].set_value(3)

    brd.board[3][3].set_letters("a")
    brd.board[3][3].set_value(1)

    my_solver = Solver()
    results = my_solver.solve(word_tree, word_list, brd)

    # If no duplicates, expecting 273 results
    print("----------------------------------------")
    print("Integrated board solving test #2")
    print("----------------------------------------")
    print("Expected results length: 273")
    print("Actual results length: " + str(len(results)))

if __name__ == "__main__":
    test()