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

    my_solver = Solver()
    results = my_solver.solve(word_tree, word_list, brd)

    # If no duplicates, expecting 89 results
    print("----------------------------------------")
    print("Integrated board solving test #2")
    print("----------------------------------------")
    print("Expected results length: 89")
    print("Actual results length: " + str(len(results)))

if __name__ == "__main__":
    test()