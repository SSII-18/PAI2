import socket;

# Se crea objeto socket
s = socket.socket()
# Se obtiene el nombre local de la maquina
host = socket.gethostname()
# Se reserva un puerto para el socket
port = 31415
# Se unen el nombre de la amquina y el puerto
s.bind((host, port))

# Se espera a que el cliente se conecte
s.listen(5)
while True:
    # connection es un nuevo socket para mandar y recibir. address es la direccion del otro socket en la conexion
    connection, address = s.accept()
    print 'Se ha conectado ', address
    connection.send('Oh, hi Mark !')
    connection.close()
    
