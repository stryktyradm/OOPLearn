class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.volume = a*b*c

    @classmethod
    def __validate_dimension(cls, value):
        return cls.MIN_DIMENSION <= value <=cls.MAX_DIMENSION

    def recal_volume(self):
        self.volume = self.__a * self.__b * self.__c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, other):
        if self.__validate_dimension(other):
            self.__a = other
            self.recal_volume()

    @b.setter
    def b(self, other):
        if self.__validate_dimension(other):
            self.__b = other
            self.recal_volume()

    @c.setter
    def c(self, other):
        if self.__validate_dimension(other):
            self.__c = other
            self.recal_volume()

    def __eq__(self, other):
        return self.volume == other.volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __le__(self, other):
        return self.volume <= other.volume

    def __gt__(self, other):
        return self.volume > other.volume

    def __ge__(self, other):
        return self.volume >= other.volume


class ShopItem:

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim.volume
        
lst = """- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)"""

lst_shop = []

for i in lst.split("\n"):
    item = i.strip(" -").split("; ")
    dim = map(int, item[2].strip("()").split(", "))
    lst_shop.append(ShopItem(item[0], item[1], Dimensions(*dim)))

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

