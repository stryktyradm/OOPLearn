class Viber:

    message_list = list()

    @classmethod
    def add_message(cls, msg):
        cls.message_list.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.message_list.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, count):
        for msg_ind in range(count):
            print(cls.message_list[msg_ind])

    @classmethod
    def total_messages(cls):
        return len(cls.message_list)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like
