from Board import Board
from Cell import Cell
import itertools
from Word import Word

def solve(board):
    height = len(board.board)
    width = len(board.board[0])

    # generate every valid combination between 3 and 10 letters

    all_possible_words = []

    for i in range(0, width):
        for j in range(0, height):
            all_possible_words += get_possible_words(board, i, j)

    return all_possible_words

def get_possible_words(board, x, y):
    """
    Args:
        board (Board) where to generate words from
        x (int) x coordinate of root cell
        y (int) y coordinate of root cell
    """
    target_cell = board.board[x][y]
    letter_choices = board.get_neighbors(target_cell)

    possible_words = []

    # TODO complete this algorithm
    # Currently just generates 2-letter 'words'
    for i in letter_choices:
        working_word = Word()
        working_word.add_cell(target_cell)
        working_word.add_cell(i)
        possible_words.append(working_word)

    return possible_words