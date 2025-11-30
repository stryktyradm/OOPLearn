class Thing:

    def get_id():
        obj_id = 0
        while True:
            obj_id += 1
            yield obj_id

    _id = get_id()

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.id = next(self._id)
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return (val for val in self.__dict__.values())


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight=weight, dims=dims)


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)

