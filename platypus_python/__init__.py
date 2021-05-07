import requests

class Server:
    def __init__(self, platypus, host, port, digest=None):
        self.platypus = platypus
        self.host = host
        self.port = port
        self.digest = digest
        self.debug = platypus.debug

    def create(self):
        assert self.digest == None
        url = "{}/api/server".format(self.platypus.url)
        if self.debug: print(url)
        data = {
            "host": self.host, 
            "port": self.port,
        }
        if self.debug: print(data)
        response = requests.post(url, data=data).json()
        if self.debug: print(response)
        assert response["status"]
        server = response["msg"]
        self.digest = server["hash"]

    def delete(self):
        assert self.digest != None
        url = "{}/api/server/{}".format(self.platypus.url, self.digest)
        if self.debug: print(url)
        response = requests.delete(url).json()
        if self.debug: print(response)
        assert response['status']
        return response['status']

    def get_clients(self):
        url = "{}/api/server/{}/client".format(self.platypus.url, self.digest)
        if self.debug: print(url)
        response = requests.get(url).json()
        if self.debug: print(response)
        assert response['status']
        result = []
        for digest, client in response['msg'].items():
            result.append(Client(
                self,
                digest,
                client['host'],
                client['port'],
                client['python2'],
                client['python3'],
            ))
        return result

    def __str__(self):
        return "[{}] {}:{}".format(self.digest, self.host, self.port)

    def __repr__(self):
        return str(self)

class Client:
    def __init__(self, server, digest, host, port, python2, python3):
        self.server = server
        self.digest = digest
        self.host = host
        self.port = port
        self.python2 = python2
        self.python3 = python3
        self.debug = server.debug

    def delete(self):
        url = "{}/api/client/{}".format(self.server.platypus.url, self.digest)
        if self.debug: print(url)
        response = requests.delete(url).json()
        if self.debug: print(response)
        assert response['status']
        return response['status']

    def system(self, cmd):
        url = "{}/api/client/{}".format(self.server.platypus.url, self.digest)
        if self.debug: print(url)
        response = requests.post(url, data={"cmd": cmd}).json()
        if self.debug: print(response)
        assert response['status']
        return response["msg"]

    def __str__(self):
        return "[{}] {}:{}\nPython2: {}\nPython3: {}".format(
            self.digest, 
            self.host, 
            self.port,
            self.python2,
            self.python3,
        )

    def __repr__(self):
        return str(self)

class Platypus:
    def __init__(self, host, port, debug=False):
        self.host = host
        self.port = port
        self.url = "http://{}:{}".format(self.host, self.port)
        self.debug = debug

    def create_server(self, host, port):
        server = Server(self, host, port)
        server.create()
        return server

    def get_server(self, digest):
        url = "{}/api/server/{}".format(self.url, digest)
        if self.debug: print(url)
        response = requests.get(url).json()
        if self.debug: print(response)
        assert response['status']
        server = Server(self, response['msg']['host'], response['msg']['port'], digest)
        return server

    def get_servers(self):
        url = "{}/api/server".format(self.url)
        if self.debug: print(url)
        response = requests.get(url).json()
        if self.debug: print(response)
        assert response['status']
        result = []
        for digest, server in response['msg']['servers'].items():
            result.append(Server(
                self,
                server['host'],
                server['port'],
                digest,
            ))
        return result

    def delete_server(self, digest):
        return self.get_server(digest).delete()

    def __str__(self):
        return "Platypus RESTful API EndPoint: {}".format(self.url)

    def __repr__(self):
        return str(self)
