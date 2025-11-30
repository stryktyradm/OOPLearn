import random

class RandomPassword:
    def __init__(self, psw_chars="qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", min_length=5, max_length=20):
        self.psw_chars = list(psw_chars)
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        length = random.randint(self.min_length, self.max_length)
        random.shuffle(self.psw_chars)
        new_password = ''.join([random.choice(self.psw_chars) for _ in range(length)])
        return new_password


rnd = RandomPassword()
lst_pass = [rnd() for _ in range(3)]
