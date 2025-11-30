class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError('request не является словарем')
        url = request.get('url', None)
        if url is None:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: {url}"

    def render_request(self, request, method):
        if method in self.methods:
            return self.__getattribute__(method.lower())(request)
        raise TypeError('данный запрос не может быть выполен')

