class RadiusVector2D:

    MIN_COORD, MAX_COORD = -100, 1024

    @classmethod
    def validate(cls, value):
        if isinstance(value, (int, float)) and cls.MIN_COORD <= value <= cls.MAX_COORD:
            return True

    def __init__(self, value_x=0, value_y=0):
        if RadiusVector2D.validate(value_x) and RadiusVector2D.validate(value_y):
            self.__x = value_x
        else:
            self.__x = 0
        if RadiusVector2D.validate(value_y):
            self.__y = value_y
        else:
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if RadiusVector2D.validate(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if RadiusVector2D.validate(value):
            self.__y = value

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)

