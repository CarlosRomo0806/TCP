import socket
import sys

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ('localhost', 10000)
print(sys.stderr, 'empezando a levantar %s puerto %s' % server_address)
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)

while True:
    # Esperando conexion
    print(sys.stderr, 'Esperando para conectarse...')
    connection, client_address = sock.accept()
    
    try:
        print(sys.stderr, 'conexión desde', client_address)

        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(19)
            print(sys.stderr,  data)
            if data:
                print(sys.stderr, 'enviando mensaje de vuelta al cliente')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no hay mas datos', client_address)
                break
            
    finally:
        # Cerrando conexion
        connection.close()