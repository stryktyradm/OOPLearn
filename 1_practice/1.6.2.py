class SingletonFive:
    obj = []

    def __new__(cls, *args, **kwargs):
        if len(cls.obj) < 5:
            cls.obj.append(super().__new__(cls))
            return cls.obj[-1]
        return cls.obj[-1]

    def __init__(self, name):
        self.name = name
