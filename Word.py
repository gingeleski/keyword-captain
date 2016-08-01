class Word(object):
    word = []

    def __init__(self):
        self.word = []

    def __str__(self):
        string = []
        for cell in self.word:
            string.append(cell.get_letters())
        return ''.join(string)

    def add_cell(self, cell):
        self.word.append(cell)

    def get_length(self):
        return len(self.word)

    def get_value(self):
        total = 0
        for cell in self.word:
            total += cell.get_value()
        return total
