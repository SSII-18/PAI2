from hashlib import sha1
from hmac import new
from base64 import b64encode
from random import _urandom, Random

clave = _urandom(8)

def mensaje_transaccion(fuente, destino, cantidad, their_nonce):
    original = ', '.join([fuente, destino, str(cantidad)])
    content = bytes(original.encode('ascii'))
    their_nonce_bytes = their_nonce.to_bytes(16, byteorder='big')
    hash_object = new(bytes(0), b''.join([content, their_nonce_bytes]), sha1)
    return bytes((original + ', ').encode('ascii')) + b64encode(hash_object.digest())

def check_mensaje(mensaje, my_nonce):
    res = False
    contenido, hach = b', '.join(mensaje.split(b', ')[:-1]), mensaje.split(b', ')[-1]
    my_nonce_bytes = my_nonce.to_bytes(16, byteorder='big')
    res_hash = b64encode(new(bytes(0), b''.join([contenido, my_nonce_bytes]), sha1).digest())
    if res_hash == hach :
        res = True
    return res

def get_cantidad(mensaje):
    return int(mensaje.decode('ascii').split(', ')[2])

def generate_nonces(used_nonces):
    random = Random()
    while True:
        nonce = random.randint(1000, 9999)
        if nonce in used_nonces:
            break
    return nonce
    
msg = mensaje_transaccion('fuente', 'destino', 100, 1234) 
print(msg)
print(check_mensaje(msg, 1234))
    

