import socket
import pickle


class Network:

    @classmethod
    def connect(cls):
        cls.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.server = "192.168.1.110"
        cls.port = 5555
        cls.addr = (cls.server, cls.port)
        try:
            cls.client.connect(cls.addr)
        except:
            print("error! : couldn't connect")

    @classmethod
    def send_str(cls, data):
        try:
            cls.client.send(str.encode(data))
            response = cls.client.recv(2048).decode()
            return response

        except socket.error as e:
            print(e)
            return "400,"

    @classmethod
    def send_obj(cls, data):
        try:
            cls.client.send(pickle.dumps(data))
        except:
            print("error! : couldn't sent object")

    @classmethod
    def receive_data(cls):
        try:
            while True:
                data = pickle.loads(cls.client.recv(2048))

        except:
            print("error! : can't receive data!")

