class Model:
    def __init__(self):
        self.data = {}

    def query(self, **kwargs):
        self.data.update(kwargs)

    def __str__(self):
        if not self.data:
            return 'Model'
        return f'''Model: {", ".join(f'{key} = {self.data[key]}' for key in self.data.keys())}'''


model = Model()
model.query(id=1, fio='Sergey', old=33)
