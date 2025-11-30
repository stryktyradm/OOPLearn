class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if 0 <= new_width <= 100:
            self.__width = new_width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if 0 <= new_height <= 100:
            self.__height = new_height
            self.show()

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')
