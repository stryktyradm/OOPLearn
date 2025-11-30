class DataBase:
    
    def __init__(self, path):
        self.path = path

    def write(self, record):
        pass

    def read(self, pk):
        pass


class Record:

    __record_pk = 0

    def __init__(self, fio, descr, old):
        self.__record_pk += 1
        self.pk = self.__record_pk
        self.fio = fio
        self.descr = descr
        self.old = old

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.fio.lower(), self.old))


