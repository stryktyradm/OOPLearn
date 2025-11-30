text = input()

class Morph:

    def __init__(self, *args):
        self.words = list(args)

    def add_word(self, word):
        self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
       return True if other.lower() in self.words else False

s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

counter = 0
for word in text.strip('.').split():
    for morph in dict_words:
        if morph == word:
            counter += 1

print(counter)

