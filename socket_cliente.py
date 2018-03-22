import socket
from transacciones import mensaje_transaccion, generate_nonces, generar_claves_firma
from time import sleep
from Crypto.PublicKey import RSA

s = socket.socket()
host = socket.gethostbyaddr('127.0.0.1')[0]
port = 31415
nonces = [None, None]
used_nonces = []
nonce_cliente = None
mensaje = b''
clave_privada_cliente = None
clave_publica_cliente = None
clave_publica_servidor = None


s.connect((host, port))
print('Se ha conectado')
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
# Recibe la clave publica del servidor #
while True:
    rec = ''
    rec = s.recv(10240)
    if rec:
        print(rec)
        clave_publica_servidor = RSA.importKey(rec)
        print('Se ha recibido la clave publica del servidor : ' + str(clave_publica_servidor))
        break
# Genera sus claves y manda su clave publica al servidor #
clave_privada_cliente, clave_publica_cliente = generar_claves_firma()
export_publica = clave_publica_cliente.exportKey('DER')
s.send(export_publica)
sleep(5)
# Manda el mensaje al servidor #
while True:
    mensaje_local = mensaje_transaccion('Mi cuenta', 'Tu cuenta', 100, nonces[1], clave_privada_cliente)
    mensaje = mensaje_local
    s.send(mensaje_local)
    print('Se ha enviado el mensaje')
    break
# Se espera confirmacion #
while True:
    rec = ''
    rec = s.recv(1024)
    if rec:
        print(rec.decode())
        break
s.close()



sleep(7)
# Se abre una nueva conexion #
s = socket.socket()
# A partir de aqui el cliente es el hacker  #
s.connect((host, port))
print('Se ha conectado')
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
sleep(5)
nonces[0] = generate_nonces(used_nonces)
s.send(bytes(str(nonces[0]).encode('ascii')))
# Recibe la clave publica del servidor #
while True:
    rec = ''
    rec = s.recv(10240)
    if rec:
        print(rec)
        clave_publica_servidor = RSA.importKey(rec)
        print('Se ha recibido la clave publica del servidor : ' + str(clave_publica_servidor))
        break
# Genera sus claves y manda su clave publica al servidor #
clave_privada_cliente, clave_publica_cliente = generar_claves_firma()
export_publica = clave_publica_cliente.exportKey('DER')
s.send(export_publica)
sleep(5)
# Manda el mensaje al servidor #
while True:
    s.send(mensaje)
    print('Se ha enviado el mensaje')
    break
# Se espera confirmacion #
while True:
    rec = ''
    rec = s.recv(1024)
    if rec:
        print(rec.decode())
        break
s.close()