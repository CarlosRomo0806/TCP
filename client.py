import socket
import nacl.utils
import sys

def numeroAleatorio(tamaño):
    return nacl.utils.random(tamaño)

def main():
    numero = numeroAleatorio(32)
    print(numero.hex())
    
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10000)
print(sys.stderr, 'conectando a %s puerto %s' % server_address)
sock.connect(server_address)
    
def Interfaz():
    print("Números aleatorios con PyNacl")
    print("1. Comienza\n0. Terminar")
    opcion = int(input("Eliges: "))
    if opcion:
        main()
        try:
            # Enviando datos
            message = 'Este es el mensaje.  Se repitio.'
            print(sys.stderr, message)
            sock.sendall(message)

            # Buscando respuesta
            amount_received = 0
            amount_expected = len(message)
    
            while amount_received < amount_expected:
                data = sock.recv(19)
                amount_received += len(data)
                print(sys.stderr, data)

        finally:
            print(sys.stderr, 'cerrando socket')
            sock.close()
        return 1
    else:
        return 0

salir = 1
while salir:
    salir = Interfaz()


