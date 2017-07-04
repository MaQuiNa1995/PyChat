#!/usr/bin/env python
import socket

cerrarServer = false
miSocket = socket.socket()
 
#Nos conectamos al servidor con el metodo connect. Tiene dos parametros
#El primero es la IP del servidor y el segundo el puerto de conexion
miSocket.connect(("localhost", 9999))

print("Escribe Cerrar Para Parar La Conexion Con El Servidor")

while (cerrarServer==false):
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mensajeEnviar = raw_input("Mensaje a Enviar: ")
 
    #Con la instancia del objeto servidor (s) y el metodo send, enviamos el mensaje introducido
    miSocket.send(mensajeEnviar)
 
    #Si por alguna razon el mensaje es exit cerramos la conexion
    if mensajeEnviar == "exit":
        cerrarServer=true
 
#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Cerrando Conexion Con El Servidor")
 
#Cerramos la instancia del objeto servidor
miSocket.close()
