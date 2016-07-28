class Cell(object):
    letters = ''
    value = -1
    is_used = False

    # coordinates on board
    x = -1
    y = -1

    def __init__(self):
        self.letters = ''
        self.value = -1
        self.is_used = False
        self.x = -1
        self.y = -1

    def get_letters(self):
        return self.letters

    def get_value(self):
        return self.value

    def get_coordinates(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y