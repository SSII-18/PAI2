import socket
from transacciones import mensaje_transaccion

# Se crea objeto socket
s = socket.socket()
# Se obtiene el nombre local de la maquina
host = socket.gethostbyaddr('127.0.0.1')[0]
# Se reserva un puerto para el socket
port = 31415
# Se unen el nombre de la maquina y el puerto
s.bind((host, port))

# Se espera a que el cliente se conecte
s.listen(5)
while True:
    # connection es un nuevo socket para mandar y recibir. address es la direccion del otro socket en la conexion
    connection, address = s.accept()
    print('Se ha conectado ', address)
    connection.send(mensaje_transaccion('Mi cuenta', 'Tu cuenta', 100))
    print('Se ha enviado el mensaje')
    break
while True:
    pass
connection.close()
    
