class HandlerGET:
    def __init__(self, func):
        self._func = func

    def get(self, func, request, *args, **kwargs):
        method = request.get('method', 'GET')
        if method == 'GET':
            return method + ': ' + func(request)

    def __call__(self, request):
        func = self._func
        return self.get(func, request)

@HandlerGET
def contact(request):
    return 'Сергей Балакирев'


# contact = HandlerGET(contact)
res = contact({"url": "contact.html"})
# res = contact({"method": "POST", "url": "contact.html"})
