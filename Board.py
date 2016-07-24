from Cell import Cell

class Board(object):
    board = []

    def __init__(self):
        self.board = []
        for i in range(5):
            cl = []
            for j in range(5):
                cl.append(Cell())
            self.board.append(cl)