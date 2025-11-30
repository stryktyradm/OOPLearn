class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    def __init__(self, *args):

        if isinstance(args[0], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            sp, ep = Point(args[0], args[1]), Point(args[2], args[3])
            self.__sp = sp
            self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def draw(self):
        print(f"Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}")


rect = Rectangle(Point(0, 0), Point(20, 34))

rect.set_coords(Point(0,0), Point(1,1))

print(isinstance(rect, Rectangle))

print(hasattr(Rectangle, 'set_coords'))

print(hasattr(Rectangle, 'get_coords'))

print(hasattr(Rectangle, 'draw'))

print(rect.get_coords())

rect.draw()