import socket
from transacciones import check_mensaje, get_cantidad

s = socket.socket()
host = socket.gethostbyaddr('127.0.0.1')[0]
print(socket.gethostbyname(socket.getfqdn()))
port = 31415

dinero = 1000

s.connect((host, port))
print('Se ha conectado')
# El numero indica el tamanno de buffer
while True:
    rec = ''
    rec = s.recv(1024)
    if rec:
        check = check_mensaje(rec)
        if check:
            dinero = dinero + get_cantidad(rec)
        print('Se ha recibido el mensaje')
        print('Dinero en cuenta : ' + str(dinero))
        print(rec)
        
s.close()

