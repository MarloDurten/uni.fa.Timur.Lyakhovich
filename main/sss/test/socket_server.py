import socket
import os

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))

s.listen(1)

conn, addr= s.accept()

file_name = s.recv(1024).decode()
print(file_name)






