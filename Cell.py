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

    def set_letters(self, letters, value=-1):
        """
        Setter method for letter(s) in this cell, can optionally
        specify the score value at the same time.

        Args:
            letters (string) - one to two letters contained in this cell
            value (int) - *optional* the score value of this cell
        """
        self.letters = letters
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_coordinates(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
