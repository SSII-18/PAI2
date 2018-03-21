import socket
from transacciones import check_mensaje, get_cantidad, generate_nonces
from time import sleep
import sys 
# Se crea objeto socket
s = socket.socket()
# Se obtiene el nombre local de la maquina
host = socket.gethostbyaddr('127.0.0.1')[0]
# Se reserva un puerto para el socket
port = 31415
# Se unen el nombre de la maquina y el puerto
s.bind((host, port))
nonces = [None, None]
used_nonces = []

dinero = 1000

# Se espera a que el cliente se conecte
s.listen(5)
print "----------Esperando conexion del cliente-----------"

# connection es un nuevo socket para mandar y recibir. address es la direccion del otro socket en la conexion
connection, address = s.accept()
sleep(5)

# El servidor genera y manda su nonce #
nonces[0] = generate_nonces(used_nonces)
connection.send(bytes(str(nonces[0]).encode('ascii')))

# Recibe el nonce del cliente #
while True:
    rec = ''
    rec = connection.recv(1024)
    if rec:
        nonce_cliente = int(rec.decode())
        if nonce_cliente:
            nonces[1] = nonce_cliente
        print('Se ha recibido el nonce del cliente : ' + str(nonce_cliente))
        break
    
# El servidor recibe el mensaje del cliente #
while True:
    rec = ''
    rec = connection.recv(1024)
    if rec:
        check = check_mensaje(rec, nonces[0])
        if check:
            local_dinero = dinero
            dinero = local_dinero + get_cantidad(rec)
        print('Se ha recibido el mensaje '+rec)
        print('Dinero en cuenta : ' + str(dinero))
        break
    
# Antes de cerrar la conexion, se marca el nonce del servidor como usado #
used_nonces.append(nonces[0])
nonces = [None, None]
connection.close()

print "--------------Abriendo nueva conexion con atacante-----------------"
print "En estos momentos el nonce del servidor es distinto, por lo que este"
print "dectectara mensajes enviados con nonces anteriores, es decir, detectara"
print "cuando se produce un ataque."

# Se abre una nueva conexion #
s = socket.socket()
s.bind((host, port))

# Se inicia la conexion con el atacante #
s.listen(20)
connection, address = s.accept()

# El servidor genera y manda su nonce #
nonces[0] = generate_nonces(used_nonces)
connection.send(bytes(str(nonces[0]).encode('ascii')))

# Recibe el nonce del cliente #
while True:
    rec = ''
    rec = connection.recv(1024)
    if rec:
        nonce_cliente = int(rec.decode())
        if nonce_cliente:
            nonces[1] = nonce_cliente
        print('Se ha recibido el nonce del cliente : ' + str(nonce_cliente)+"\n")
        break
    
i = 0   
while True:
    i+=1
    print("Dinero en la cuenta "+str(dinero))
    rec = ''
    rec = connection.recv(1024)
    print "Se ha recibido el mensaje "+rec
    
    if rec:
        check = check_mensaje(rec, nonces[0])
        
        if check:
            local_dinero = dinero
            dinero = local_dinero + get_cantidad(rec)
        else:
            print >>sys.stderr, 'Se ha detectado un ataque, mensaje '+rec+" descartado"
            
        print('Dinero en cuenta : ' + str(dinero)+"\n")
        
    if (i == 2):
        break
        
connection.close()
