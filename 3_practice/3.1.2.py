class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    PRODUCT_ID = 0

    def __new__(cls, *args, **kwargs):
        cls.PRODUCT_ID += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = self.PRODUCT_ID
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if not (key in ('id', 'weight', 'price') and isinstance(value, (int, float)) and value >= 0 or key in ('name') and isinstance(value, str)):
            raise TypeError("Неверный тип: присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        return object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
