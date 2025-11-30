class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.cnt = 0

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head, self.tail = obj, obj
        else:
            obj.prev = self.tail
            self.tail.next, self.tail = obj, obj
        self.cnt += 1

    def get_obj_index(self, indx):
        if indx <= self.cnt:
            obj = self.head
            while indx != 0:
                obj = obj.next
                indx -= 1
            return obj

    def remove_obj(self, indx):
        obj = self.get_obj_index(indx)
        if obj == self.head:
            self.head = obj.next
            self.head.prev = None
        elif obj == self.tail:
            obj.prev.next, self.tail = None, obj.prev
        else:
            obj.prev.next, obj.next.prev = obj.next, obj.prev
        self.cnt -= 1

    def __len__(self):
        return self.cnt

    def __call__(self, indx):
        obj = self.get_obj_index(indx)
        return obj.data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Danya"))
linked_lst.remove_obj(1)
n = len(linked_lst)  # n = 1
