from hashlib import sha1
from hmac import new
from base64 import b64encode
from random import _urandom

clave = _urandom(8)

def mensaje_transaccion(fuente, destino, cantidad):
    original = ', '.join([fuente, destino, str(cantidad)])
    hash_object = new(bytes(0), bytes(original.encode('ascii')), sha1)
    return bytes((original + ', ').encode('ascii')) + b64encode(hash_object.digest())

def check_mensaje(mensaje):
    contenido, hach = b', '.join(mensaje.split(b', ')[:3]), mensaje.split(b', ')[3]
    res = b64encode(new(bytes(0), contenido, sha1).digest())
    return res == hach

def get_cantidad(mensaje):
    return int(mensaje.decode('ascii').split(', ')[2])
    
    

