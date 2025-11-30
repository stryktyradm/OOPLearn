class AppStore:

    def __init__(self):
        self.application = dict()

    def add_application(self, app):
        self.application[app] = app.__dict__

    def remove_application(self, app):
        self.application.pop(app)

    def block_application(self, app):
        self.application[app]['blocked'] = True

    def total_apps(self):
        return len(self.application)


class Application:

    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked
        