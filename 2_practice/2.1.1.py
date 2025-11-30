class Clock:

    @staticmethod
    def __check_time(tm):
        return True if type(tm) is int and 0 <= tm < 100000 else False

    def __init__(self, time):
        if self.__check_time:
            self.__time = time
        else:
            self.__time = 0

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm    

    def get_time(self):
        return self.__time


clock = Clock(4530)
