class Word(object):
    word = []

    def __init__(self):
        self.word = []

    def add_cell(self,cell):
        self.word.append(cell)

    def get_string(self):
        string = []
        for cell in self.word:
            string.append(cell.get_letters())
        return ''.join(string)

    def get_value(self):
        total = 0
        for cell in self.word:
            total += cell.get_value()
        return total