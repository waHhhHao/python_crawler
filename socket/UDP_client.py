from socket import *
from threading import Thread


# s = socket()

class Server(Thread):
    def __init__(self, name, IP, PORT_REC, BUFLEN):
        super().__init__()
        self.setName(name)
        self.BUFLEN = BUFLEN
        self.ss = socket(AF_INET, SOCK_DGRAM)
        self.ss.bind((IP, PORT_REC))

    def run(self):
        while True:
            recved, add = self.ss.recvfrom(self.BUFLEN)
            print(f'{self.getName()} recive from {add}, msg={recved.decode()}')
            if recved.decode() == 'exit':
                break
        self.ss.close()


class Client(Thread):
    def __init__(self, name, IP, PORT_SEND):
        super().__init__()
        self.setName(name)
        self.sc = socket(AF_INET, SOCK_DGRAM)
        self.IP = IP
        self.PORT_SEND = PORT_SEND

    def run(self):
        while True:
            data = input('>>> ')
            self.sc.sendto(data.encode(), (self.IP, self.PORT_SEND))
            if data == 'exit':
                break
        self.sc.close()


if __name__ == '__main__':
    IP = '127.0.0.1'
    PORT_REC = 9999
    PORT_SEND = 8888
    BUFLEN = 1024

    ss1 = Server('ss1', IP, PORT_REC, BUFLEN)
    sc1 = Client('sc1', IP, PORT_SEND)
    ss1.start()
    sc1.start()
    ss1.join()
    sc1.join()
