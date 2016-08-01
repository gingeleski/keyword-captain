from Board import Board
from Cell import Cell
import itertools
from Word import Word

def solve(word_tree, board):
    height = len(board.board)
    width = len(board.board[0])
    results_list = dict()
    for root_position in [ (x, y) for x in range(width) for y in range(height) ]:
        explore_words(word_tree, board, [root_position], results_list)
    results = results.items()
    results.sort(cmp=lambda a,b: -cmp(len(a[0]), len(b[0])))
    return results

def explore_words(word_tree, board, positions_list, results_list):
    word = "".join(board.board[p].get_string() for p in positions_list)
    sub_tree = tree_search(word_tree, word)
    if sub_tree == {}:
        return
    if True in sub_tree:
        if len(word) >= 3:
            results[word] = positions_list
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
    if word == "":
        return tree
    head, tail = word[0], word[1:]
    if head not in tree:
        return {}
    return tree_search(word_tree[head], tail)
