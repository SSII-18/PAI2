from hashlib import sha1
from hmac import new
from base64 import b64encode, b64decode
from random import _urandom, Random
from Crypto.PublicKey import RSA

# Digital signature #
# https://stackoverflow.com/questions/4232389/signing-and-verifying-data-using-pycrypto-rsa #

clave = _urandom(8)

def mensaje_transaccion(fuente, destino, cantidad, their_nonce, clave_privada):
    original = ', '.join([fuente, destino, str(cantidad)])
    content = bytes(original.encode('ascii'))
    their_nonce_bytes = their_nonce.to_bytes(16, byteorder='big')
    hash_object = new(bytes(0), b''.join([content, their_nonce_bytes]), sha1)
    hash_msg = hash_object.digest()
    firma = clave_privada.sign(hash_msg, '')[0]
    firma_bytes = bytes(str(firma).encode('ascii'))
    return bytes((original + ', ').encode('ascii')) + b64encode(hash_msg) + b', ' + firma_bytes

def check_mensaje(mensaje, my_nonce, clave_publica):
    res = False
    contenido, hach, firma_bytes = b', '.join(mensaje.split(b', ')[:-2]), mensaje.split(b', ')[-2], mensaje.split(b', ')[-1]
    my_nonce_bytes = my_nonce.to_bytes(16, byteorder='big')
    res_hash_bytes = new(bytes(0), b''.join([contenido, my_nonce_bytes]), sha1).digest()
    res_hash = b64encode(res_hash_bytes)
    firma = int(firma_bytes.decode())
    if res_hash == hach and clave_publica.verify(res_hash_bytes, (firma,)):
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

def generar_claves_firma():
    private_key = RSA.generate(2048, _urandom)
    public_key = private_key.publickey()
    return private_key, public_key

# hash = 'W31BLOJ5FkBNuCbeVgHOXoUfrjY='
# private_key, public_key = generar_claves_firma()
# export_public = public_key.exportKey('DER')
# import_public = RSA.importKey(export_public)
# firma = private_key.sign(b64decode(hash), '')
# res = import_public.verify(b64decode(hash), firma)
# print(firma)
# print(type(firma[0]))
# print(res)
