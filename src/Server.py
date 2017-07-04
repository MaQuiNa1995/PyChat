#!/usr/bin/env python
import socket

PUERTO = 9999
MAX_CONEXIONES = 1
# Está en blanco porque queremos aceptar cualquier conexión
CLIENTE_PREDETERMINADO = ""
 
#instanciamos un objeto para trabajar con el socket
miSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#Con bind le indicamos que puerto debe escuchar y de que cliente esperar conexiones
# (Dejarlo En Blanco) para recibir conexiones externas todas
miSocket.bind(CLIENTE_PREDETERMINADO, PUERTO)
 
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
miSocket.listen(MAX_CONEXIONES)
 
#Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
puerto, arrayClientes = miSocket.accept()
 
 
while True:
 
    #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
    #la cantidad de bytes para recibir
    recibido = puerto.recv(1024)
 
    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "Cerrar":
        break
 
    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print str(arrayClientes[0]) + " Dice: ", recibido
 
    #Devolvemos el mensaje al cliente
    puerto.send(recibido)


print("Cerrando Servidor")

#Cerramos la instancia del socket cliente y servidor
puerto.close()
miSocket.close()
