import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

not_open = sock.connect_ex(('127.0.0.1',80))

if not_open == 0:
   print('Open')
else:
   print('Not Open')

sock.close()