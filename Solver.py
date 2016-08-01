from Board import Board
from Cell import Cell
import itertools
from Word import Word

WORD_MIN_LENGTH = 3
WORD_MAX_LENGTH = 10

results_list = []

def solve(word_tree, board):
    # TODO fix function bug - returning nothing, though generates results inproc
    height = len(board.board)
    width = len(board.board[0])
    results_list = []
    for root_position in [ (x, y) for x in range(width) for y in range(height) ]:
        explore_words(word_tree, board, [root_position])
        # TODO fix bug where results_list goes to zero here
    return results_list

def explore_words(word_tree, board, positions_list):
    word = Word()
    for px, py in positions_list:
        word.add_cell(board.board[px][py])
    sub_tree = tree_search(word_tree, word)
    if sub_tree == {}:
        return
    #if True in sub_tree:
    if WORD_MAX_LENGTH >= word.get_length() >= WORD_MIN_LENGTH:
            results_list.append(word)
    x, y = positions_list[-1]
    for (dx, dy) in [ (dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] ]:
        nx, ny = x+dx, y+dy
        # Check if new position is outside board
        x_limit = len(board.board[0])
        y_limit = len(board.board)
        if nx not in range(x_limit) or ny not in range(y_limit):
            continue
        # Don't reuse positions
        if (nx, ny) in positions_list:
            continue
        explore_words(word_tree, board, positions_list + [(nx, ny)])

def tree_search(word_tree, word):
    word_str = str(word)
    if word_str == "":
        return word_tree
    head, tail = word_str[0], word_str[1:]
    if head not in word_tree:
        return {}
    return tree_search(word_tree[head], tail)
