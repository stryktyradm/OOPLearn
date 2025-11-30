class ImageFileAcceptor:
    def __init__(self, extension):
        self.extension = extension

    def __call__(self, *args, **kwargs):
        return True if args[0].split('.')[-1] in self.extension else False


filenames = ["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
