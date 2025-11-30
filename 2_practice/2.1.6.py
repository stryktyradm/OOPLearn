class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.get_next().set_prev(None)
            self.tail.set_next(None)

    def get_data(self):
        lst = []
        obj = self.head
        while obj:
            lst.append(obj.get_data())
            obj = obj.get_next()
        return lst


class ObjList:

    def __init__(self, data, next=None, prev=None):
        self.__next = next
        self.__prev = prev
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.remove_obj()
lst.remove_obj()
lst.remove_obj()
res = lst.get_data()
print(res)
