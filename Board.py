from Cell import Cell

class Board(object):
    board = []

    def __init__(self, size):
        self.board = []
        for i in range(size):
            cl = []
            for j in range(size):
                this_cell = Cell()
                this_cell.set_x(i)
                this_cell.set_y(j)
                cl.append(this_cell)
            self.board.append(cl)
    
    def get_neighbors(self, cell):
        neighbors = []
        x, y = cell.get_coordinates()
        
        for col in range(x-1, x+2):
            for row in range(y-1, y+2):
                if col >= 0 and col < len(self.board[0]):
                    if row >= 0 and row < len(self.board):
                        if col == x and row == y:
                            pass
                        else:
                            neighbors.append(self.board[col][row])

        return neighbors