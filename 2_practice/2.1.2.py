class Money:

    def __init__(self, money):
        self.__money = money

    @staticmethod
    def __check_money(money):
        return True if type(money) is int and money >= 0 else False

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()
m2 = mn_2.get_money()
