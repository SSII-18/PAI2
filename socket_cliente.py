import socket
from transacciones import mensaje_transaccion, generate_nonces
from time import sleep

s = socket.socket()
host = socket.gethostbyaddr('127.0.0.1')[0]
port = 31415
nonces = [None, None]
used_nonces = []
nonce_cliente = None
mensaje = b''

s.connect((host, port))
print('-----------------Estableciendo conexion como cliente-----------------')

# Recibe el nonce del servidor #
while True:
    rec = ''
    rec = s.recv(1024)
    if rec:
        nonce_serv = int(rec.decode())
        if nonce_serv:
            nonces[1] = nonce_serv
        print('Se ha recibido el nonce del servidor : ' + str(nonce_serv))
        break
    
# Genera y manda su nonce al servidor #
nonces[0] = generate_nonces(used_nonces)
sleep(5)
s.send(bytes(str(nonces[0]).encode('ascii')))

# Manda el mensaje al servidor #
while True:
    mensaje_local = mensaje_transaccion('Mi cuenta', 'Tu cuenta', 100, nonces[1])
    mensajeReplay = mensaje_local
    mensajeMITM =  mensaje_transaccion('Mi cuenta', 'Tu cuenta', 200, nonces[1])
    s.send(mensaje_local)
    print('Se ha enviado el mensaje '+mensaje)
    break

s.close()

sleep(7)
# Se abre una nueva conexion #
s = socket.socket()

# A partir de aqui el cliente es el hacker  #
s.connect((host, port))
print('---------------Estableciendo conexion como atacante--------------------')

# Recibe el nonce del servidor #
while True:
    rec = ''
    rec = s.recv(1024)
    if rec:
        nonce_serv = int(rec.decode())
        if nonce_serv:
            nonces[1] = nonce_serv
        print('Se ha recibido el nonce del servidor : ' + str(nonce_serv)+"\n")
        break
# Genera y manda su nonce al servidor #
sleep(5)
nonces[0] = generate_nonces(used_nonces)
s.send(bytes(str(nonces[0]).encode('ascii')))
sleep(5)

# Manda el mensaje al servidor #
print "Enviando mensaje para simular ataque de replay"
print "Dicho mensaje es el mismo que el enviado anteriormente, con el mismo nonce"
s.send(mensajeReplay)
print('Se ha enviado el mensaje '+mensajeReplay+"\n")

print "Enviando mensaje para simular ataque de MITM"
print "Dicho mensaje es distinto que el enviado anteriormente, con el mismo nonce"
s.send(mensajeMITM)
print('Se ha enviado el mensaje '+mensajeMITM)

s.close()