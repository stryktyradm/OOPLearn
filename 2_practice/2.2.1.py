class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 100:
            self.__model = name


car = Car()
car.model = 'BMV'
print(car.model)