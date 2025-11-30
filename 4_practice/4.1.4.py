class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name = args[0]
        return cls.__instance

    def __del__(self):
        Singleton.__instance = None


class Game(Singleton):
    pass

