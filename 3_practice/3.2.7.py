class Handler:
    def __init__(self, methods=('GET', )):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method in self.methods:
                if method == 'GET':
                    return self.get(func, request, method)
                if method == 'POST':
                    return self.post(func, request, method)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return args[0] + ': ' + func(request)

    def post(self, func, request, *args, **kwargs):
        return args[0] + ': ' + func(request)

# @Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


contact = Handler(methods=('GET', 'POST'))(contact)
res = contact({})
