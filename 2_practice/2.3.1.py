class FloatType:

    @classmethod
    def check_type(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, name, owner):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, new_value):
        self.check_type(new_value)
        instance.__dict__[self.name] = new_value


class Cell:

    value = FloatType()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, rows, columns):
        self.cells = [[Cell() for _ in range(columns)] for _ in range(rows)]


if __name__ == '__main__':
    table = TableSheet(5, 3)
    val = 1
    for row in table.cells:
        for cell in row:
            cell.value += val
            val += 1
