class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for side in self.__dict__:
            if not (isinstance(self.__dict__[side], int) or isinstance(self.__dict__[side], float)) or self.__dict__[side] <= 0:
                return 1
            side_length = self.__dict__.pop(side)
            if side_length >= sum(self.__dict__.values()):
                return 2
            self.__dict__[side] = side_length
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
