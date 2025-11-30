class Server:

    servers_ip = list()

    def __init__(self):
        self.ip = self.count_ip_address()
        self.buffer = list()
        self.send_buffer = list()

    @classmethod
    def count_ip_address(cls):
        ip_address = len(cls.servers_ip) + 1
        cls.servers_ip.append(ip_address)
        return ip_address

    def send_data(self, data):
        self.send_buffer.append(data)

    def get_data(self):
        lst = self.buffer.copy()
        self.buffer.clear()
        return lst

    def get_ip(self):
        return self.ip

class Router:

    def __init__(self):
        self.buffer = list()
        self.servers = dict()

    def link(self, server):
        self.servers[server.ip] = server
        self.buffer.append(server.send_buffer)

    def unlink(self, server):
        self.servers.pop(server.ip)

    def send_data(self):
        for server_buffer in self.buffer:
            for data in server_buffer:
                self.servers[data.ip].buffer.append(data)
        self.buffer.clear()


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
print(router.servers)
print(router.buffer)
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_to[0].data)
print(msg_lst_from[0].data)
