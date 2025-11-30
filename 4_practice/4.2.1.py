class ListInteger(list):
    def __init__(self, data):
        super().__init__(data)

    def is_valid(self, data):
        if isinstance(data, int):
            return True
        raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        if self.is_valid(value):
            super().__setitem__(key, value)

    def append(self, value):
        if self.is_valid(value):
            super().append(value)

