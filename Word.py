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
        word_multiplier = 1
        for cell in self.word:
            if cell.get_multiplier() == 'DW':
                # Double word multiplier is active
                word_multipler *= 2
            elif cell.get_multiplier() == 'TW':
                # Triple word multiplier is active
                word_multiplier *= 3
            total += cell.get_value()
        return (total * word_multiplier)
