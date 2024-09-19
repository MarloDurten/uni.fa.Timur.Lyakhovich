import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030)) # Подключаемся к нашему серверу.


file = open('C:\\Users\\user\\Documents\\GitHub\\uni.fa.Timur.Lyakhovich\main\\sss\\test\\file.csv', 'rb')


data = file.read()
s.sendall(data)
s.send(b'<END>')

file.close()
s.close()