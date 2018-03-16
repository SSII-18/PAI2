import socket

s = socket.socket()
host = socket.gethostname()
port = 31415

s.connect((host, port))
# El numero indica el tamanno de buffer
print s.recv(1024)
s.close()

