from hashlib import sha1
from hmac import new
from base64 import b64encode, b64decode
from random import _urandom, Random
from _sha256 import sha256

# Digital signature #
# https://stackoverflow.com/questions/4232389/signing-and-verifying-data-using-pycrypto-rsa #

clave = _urandom(8)

def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]

def mensaje_transaccion(fuente, destino, cantidad, their_nonce):
    original = ', '.join([fuente, destino, str(cantidad)])
    content = bytes(original.encode('ascii'))
    their_nonce_bytes = to_bytes(their_nonce, 16)
    hash_object = new(bytes(0), b''.join([content, their_nonce_bytes]), sha256)
    return bytes((original + ', ').encode('ascii')) + b64encode(hash_object.digest())

def check_mensaje(mensaje, my_nonce):
    res = False
    contenido, hach = b', '.join(mensaje.split(b', ')[:-1]), mensaje.split(b', ')[-1]
    my_nonce_bytes = to_bytes(my_nonce, 16)
    res_hash = b64encode(new(bytes(0), b''.join([contenido, my_nonce_bytes]), sha256).digest())
    if res_hash == hach :
        res = True
    return res

def get_cantidad(mensaje):
    return int(mensaje.decode('ascii').split(', ')[2])

def generate_nonces(used_nonces):
    random = Random()
    while True:
        nonce = random.randint(1, pow(2, 16)-1)
        if not nonce in used_nonces:
            break
    return nonce

def generar_firma():
    pass

