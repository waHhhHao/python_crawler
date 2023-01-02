from socket import *
from threading import Thread


def recieve_data(data_socket: socket):
    while True:
        data = data_socket.recv(1024).decode()
        if data == 'exit':
            break
        print(f'recive msg from client, msg={data}\n>>> ', end='')
    data_socket.close()


def send_data(data_socket: socket):
    while True:
        data = input('>>> ')
        data_socket.send(data.encode())
        if data == 'exit':
            break
        print(f'send {data} to client')
    data_socket.close()


IP = '127.0.0.1'
PORT_SERVER = 8888
ss = socket(AF_INET, SOCK_STREAM)
ss.bind((IP, PORT_SERVER))
ss.listen(5)
data_socket, add = ss.accept()
print(f'server connect {add}')
t1 = Thread(target=recieve_data, args=(data_socket,))
t2 = Thread(target=send_data, args=(data_socket,))
t1.start()
t2.start()
t1.join()
t2.join()
ss.close()