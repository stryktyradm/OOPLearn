import math


class Complex:
    def __init__(self, real, img):
        self._real = real
        self._img = img

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        if isinstance(value, (int, float)):
            self._real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        if isinstance(value, (int, float)):
            self._img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return math.sqrt(self.real*self.real + self.img*self.img)


cmp = Complex(7, 8)
cmp.real, cmp.img = 3, 4
c_abs = abs(cmp)
