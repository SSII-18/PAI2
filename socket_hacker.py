import socket
from time import sleep
from transacciones import mensaje_transaccion

s = socket.socket()
host = socket.gethostbyaddr('127.0.0.1')[0]
print(socket.gethostbyname(socket.getfqdn()))
port = 31415
nonces = []
used_nonces = []

mensaje_replay = b'Mi cuenta, Tu cuenta, 100, VFGkcxO7MTUpxTkeTyhbw6giXnE='

s.connect((host, port))
print('Se ha conectado')
# El numero indica el tamanno de buffer
i = 0
while True:
    s.send(mensaje_replay)
    print('Se ha enviado el mensaje')
    print(i)
    if i > 3:
        break
    sleep(5)
    i = i + 1
s.close()