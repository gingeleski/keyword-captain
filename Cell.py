from enum import Enum

class Cell(object):
    letters = ''
    value = -1
    is_used = False
    multiplier = None

    # coordinates on board
    x = -1
    y = -1

    def __init__(self):
        self.letters = ''
        self.value = -1
        self.is_used = False
        self.x = -1
        self.y = -1
        self.multiplier = None

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
        if self.multiplier == 'DL':
            # Double letter multiplier is active
            return self.value * 2
        elif self.multiplier == 'TL':
            # Triple letter multiplier is active
            return self.value * 3
        # Either there's a word multiplier or no multiplier
        return self.value

    def set_value(self, value):
        self.value = value

    def get_coordinates(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_multiplier(self, multiplier):
        """
        Valid multipliers are the following:
        DW - Double word
        TW - Triple word
        DL - Double letter
        TL - Triple letter
        """
        if multiplier != 'DW':
            if multiplier != 'TW':
                if multiplier != 'DL':
                    if multiplier != 'TL':
                        return
        self.multiplier = multiplier

    def get_multiplier(self):
        return self.multiplier
