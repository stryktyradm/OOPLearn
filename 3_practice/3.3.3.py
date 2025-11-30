class WordString:
    def __init__(self, string=''):
        self._string = string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    def __len__(self):
        return len(self.string.split())

    def __call__(self, indx):
        return self.string.split()[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")


