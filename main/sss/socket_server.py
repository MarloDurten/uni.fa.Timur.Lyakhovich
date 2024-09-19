import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
s.listen(1) # Начинаем прослушивать входящие соединения.
conn, addr = s.accept() # Метод который принимает входящее соединение.

while True:
	data = conn.recv(1024) # Получаем данные из сокета.
	if not data:
		break
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode('utf-8'))
conn.close()