class Translator:

    DICTIONARY = {}

    def add(self, eng, rus):
        if eng not in self.DICTIONARY:
            self.DICTIONARY[eng] = []
        self.DICTIONARY[eng].append(rus)

    def remove(self, eng):
        del self.DICTIONARY[eng]

    def translate(self, eng):
        return self.DICTIONARY[eng]


tr = Translator()
pairs = (('tree', 'дерево'), ('car', 'машина'), ('car', 'автомобиль'), ('leaf', 'лист'), ('river', 'река'), ('go', 'идти'), ('go', 'ехать'), ('go', 'ходить'), ('milk', 'молоко'))
for pair in pairs:
    tr.add(pair[0], pair[1])
print(*tr.translate('go'))
