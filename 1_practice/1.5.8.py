class ListObject:

    def __init__(self, data):
        self.data = data
        self.next_obj = self.link(lst_in[lst_in.index(data)])

    def link(self, obj):
        return None if lst_in.index(obj) == len(lst_in) - 1 else ListObject(lst_in[lst_in.index(obj) + 1])

    def get_data(self):
        print(self.data)
        if self.next_obj is not None: self.next_obj.get_data()


lst_in = [
          '1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)'
          ]

head_obj = ListObject(lst_in[0])
head_obj.get_data()
