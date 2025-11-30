import sys


class ShopItem:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.weight == other.weight and self.price == other.price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = dict()
for str_obj in lst_in:
    lst_obj = str_obj.split(' ')
    item = ShopItem(name=' '.join(lst_obj[:-2]).rstrip(':'),
                    weight=lst_obj[-2],
                    price=lst_obj[-1])
    if item not in shop_items:
        shop_items[item] = [item, 0]
    shop_items[item][1] += 1
