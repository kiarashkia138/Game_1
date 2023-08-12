import socket
from _thread import *
from User import User
import sys


server = "192.168.1.110"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(3)
print("server started!")


def thread_connection(connection):
    print("connected")

    run = True
    while run:
        data = connection.recv(2048).decode()
        com = data.split(",")
        res = ""

        if com[0] == "login":
            user = User.login(com[1], com[2])
            if user is not None:
                res = "200," + str(user.score)
                run = False
            else:
                res = "400,"
        else:
            if User.user_exist(com[1]):
                res = "400,"
            else:
                User(com[1], com[2], 0)
                res = "200,0"
                run = False

        connection.send(str.encode(res))


while True:
    conn, addr = s.accept()
    print("connected to : ", addr)

    start_new_thread(thread_connection, (conn,))


