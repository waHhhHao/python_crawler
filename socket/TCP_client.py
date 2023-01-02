from socket import *
from threading import Thread


def recieve_data(sc: socket):
    while True:
        data = sc.recv(1024).decode()
        if data == 'exit':
            break
        print(f'recive msg from server, msg={data}\n>>> ',end='')
    sc.close()


def send_data(sc: socket):
    while True:
        data = input('>>> ')
        sc.send(data.encode())
        if data == 'exit':
            break
        print(f'send {data} to server')
    sc.close()


IP = '127.0.0.1'
PORT_SERVER = 8888
sc = socket(AF_INET, SOCK_STREAM)
sc.connect((IP, PORT_SERVER))
print('client connect server')
t1 = Thread(target=recieve_data, args=(sc,))
t2 = Thread(target=send_data, args=(sc,))
t1.start()
t2.start()
t1.join()
t2.join()
