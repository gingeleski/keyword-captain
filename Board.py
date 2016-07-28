from Cell import Cell

class Board(object):
    board = []

    def __init__(self, size):
        self.board = []
        for i in range(size):
            cl = []
            for j in range(size):
                this_cell = Cell()
                this_cell.set_x(j)
                this_cell.set_y(i)
                cl.append(this_cell)
            self.board.append(cl)
    
    def get_neighbors(self, cell):
        neighbors = []
        for i in range(rowNumber-2, rowNumber+1):
            for j in range(columnNumber-2, columnNumber+1):
                if  i >= 0 and i < len(self.board):
                    if j >= 0 and j < len(self.board[0]):
                        neighbors.append(self.board[i][j])
        return neighbors