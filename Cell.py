class Cell(object):
    letters = None
    value = 0
    is_used = False

    def __init__(self):
        self.letters = 'X'
        self.value = 0
        self.is_used = False

    def get_letters(self):
        return self.letters

    def get_value(self):
        return self.value