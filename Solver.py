from Board import Board
from Cell import Cell
import itertools
from Word import Word

WORD_MIN_LENGTH = 3
WORD_MAX_LENGTH = 10

class Solver(object):
    results_list = []

    def __init__(self):
        self.results_list = []

    def solve(self, word_tree, word_list, board):
        height = len(board.board)
        width = len(board.board[0])
        results_list = []
        for root_position in [ (x, y) for x in range(width) for y in range(height) ]:
            self.explore_words(word_tree, board, [root_position])
        self.sanitize_results(word_list)
        self.results_list.sort(cmp=lambda a,b: -cmp(a.get_value(), b.get_value()))
        return self.results_list

    def remove_result_duplicates(self):
        """
        Removes word duplicates from the result list.
        If one instance has a higher score, that is kept.
        """
        pass # TODO

    def sanitize_results(self, word_list):
        """
        Given a word list, grooms the results list to make sure it only
        contains matches to the word list.
        """
        self.results_list = [word for word in self.results_list if str(word) in word_list]

    def explore_words(self, word_tree, board, positions_list):
        word = Word()
        for px, py in positions_list:
            word.add_cell(board.board[px][py])
        sub_tree = self.tree_search(word_tree, word)
        if sub_tree == {}:
            return
        if WORD_MAX_LENGTH >= word.get_length() >= WORD_MIN_LENGTH:
            self.results_list.append(word)
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
            self.explore_words(word_tree, board, positions_list + [(nx, ny)])

    def tree_search(self, word_tree, word):
        word_str = str(word)
        if word_str == "":
            return word_tree
        head, tail = word_str[0], word_str[1:]
        if head not in word_tree:
            return {}
        return self.tree_search(word_tree[head], tail)
