from transacciones import mensaje_transaccion, check_mensaje

def test_mensaje(): 
    mensaje_1 = mensaje_transaccion('Mark', 'Shark', 12)
    print(mensaje_1)
    print (check_mensaje(mensaje_1))
    mensaje_2 = mensaje_transaccion('Mark', 'Shark', -123)
    print(mensaje_2)
    print(check_mensaje(mensaje_2))
    mensaje_3 = mensaje_transaccion('Mark', 'Shark', -0.5)
    print(mensaje_3)
    print(check_mensaje(mensaje_3))
    
