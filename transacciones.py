from hashlib import sha1
from hmac import new, compare_digest
from base64 import b64encode, b64decode
from random import _urandom

clave = _urandom(8)

def mensaje_transaccion(fuente, destino, cantidad):
    original = ', '.join([fuente, destino, str(cantidad)])
    hash_object = new(clave, original, sha1)
    return '{0}, {1}'.format(original, b64encode(hash_object.digest()))

def check_mensaje(mensaje):
    contenido, hach = ', '.join(mensaje.split(', ')[:3]), mensaje.split(', ')[3]
    return compare_digest(b64decode(hach), new(clave, contenido, sha1).digest())

