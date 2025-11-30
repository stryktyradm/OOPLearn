class Person:
    name = "Сергей Балакирев"
    job = "Программист"
    city = "Москва"


p1 = Person()
status = True if p1.__dict__.get('job', False) else False
print(status)
