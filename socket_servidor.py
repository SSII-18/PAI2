import socket
from transacciones import mensaje_transaccion, check_mensaje, get_cantidad

# Se crea objeto socket
s = socket.socket()
# Se obtiene el nombre local de la maquina
host = socket.gethostbyaddr('127.0.0.1')[0]
# Se reserva un puerto para el socket
port = 31415
# Se unen el nombre de la maquina y el puerto
s.bind((host, port))

dinero = 1000

# Se espera a que el cliente se conecte
s.listen(5)
while True:
    # connection es un nuevo socket para mandar y recibir. address es la direccion del otro socket en la conexion
    connection, address = s.accept()
    rec = ''
    rec = connection.recv(1024)
    if rec:
        check = check_mensaje(rec)
        if check:
            local_dinero = dinero
            dinero = local_dinero + get_cantidad(rec)
        print('Se ha recibido el mensaje')
        print('Dinero en cuenta : ' + str(dinero))
        print(rec)
    break
connection.close()
s.listen(5)
connection, address = s.accept()
while True:
    print(dinero)
    # connection es un nuevo socket para mandar y recibir. address es la direccion del otro socket en la conexion
    rec = ''
    rec = connection.recv(1024)
    if rec:
        check = check_mensaje(rec)
        if check:
            local_dinero = dinero
            dinero = local_dinero + get_cantidad(rec)
        print('Se ha recibido el mensaje')
        print('Dinero en cuenta : ' + str(dinero))
        print(rec)
connection.close()
