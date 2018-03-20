import socket
from transacciones import mensaje_transaccion

s = socket.socket()
host = socket.gethostbyaddr('127.0.0.1')[0]
print(socket.gethostbyname(socket.getfqdn()))
port = 31415

s.connect((host, port))
print('Se ha conectado')
# El numero indica el tamanno de buffer
while True:
    s.send(mensaje_transaccion('Mi cuenta', 'Tu cuenta', 100))
    print('Se ha enviado el mensaje')
    break
s.close()

