stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    
    def __init__(self, lst_words):
        self.lst_words = lst_words
    
    @classmethod
    def __verify(cls, other):
        if not isinstance(other, cls):
            raise TypeError(f'Сравниваемый объект не является экземпляром класса: {cls.__name__}')
        return len(other.lst_words)

    def __eq__(self, other):
        other_st = self.__verify(other)
        return len(self.lst_words) == other_st

    def __lt__(self, other):
        other_st = self.__verify(other)
        return len(self.lst_words) < other_st

    def __le__(self, other):
        other_st = self.__verify(other)
        return len(self.lst_words) <= other_st

    def __gt__(self, other):
        other_st = self.__verify(other)
        return len(self.lst_words) > other_st

    def __ge__(self, other):
        other_st = self.__verify(other)
        return len(self.lst_words) >= other_st


lst_text = [StringText(st.strip('-?!,.').split()) for st in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(st.lst_words) for st in lst_text_sorted]

