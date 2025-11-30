from string import ascii_lowercase, digits

class EmailValidator:
    validate_char = ascii_lowercase + digits + '_' + '.'
    func = {
        'first': lambda x: True,
        'two': lambda x: True,
        'three': lambda x: True
    }

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def is_email_str(email):
        return isinstance(email, str)

    @classmethod
    def check_email(cls, email):
        if cls.is_email_str(email):
            sl = email.strip('@')
            if len(sl) == 2 and len(sl[0]) <= 100 and cls.func['first'](sl[0]) == True:
                pass
        return False

    @classmethod
    def get_random_email(cls):
        pass


em = EmailValidator()
print(em)

