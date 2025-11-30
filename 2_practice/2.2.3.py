class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_obj):
        obj = self.top
        if obj:
            while obj.next is not None:
                obj = obj.next
            obj.next = new_obj
        else:
            self.top = new_obj

    def pop(self):
        obj = self.top
        if obj:
            if obj.next is not None:
                tmp = obj
                while obj.next is not None:
                    obj, tmp = obj.next, obj
                tmp.next = None
                return obj
            self.top = None
            return obj
        return obj

    def get_data(self):
        obj, lst = self.top, list()
        while obj is not None:
            lst.append(obj.data)
            obj = obj.next
        return lst

class StackObj:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()
print(res)
