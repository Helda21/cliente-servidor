"""
Servidor para la construccion de un chat
creado por :
HELIO DAVID ESPINOSA CONTRERAS
C.C. 1010235183
24/03/2023

Este codigo es para crear un chat servidor
que corra atraves de una red local mediante protocolo tcp/ip a traves de la direccion ip

http://192.168.0.100

funciones que se usaran:
ini()esta pide al usuario la ip del host o del servidor y el puerto que tambien sockets

crearsocket() siguiendo el esquema del protocolo TCP
ligarSockets(Host, port) Une un socket a los datos que se dan para el host y port

"""

#aqui llamamos las librerias de python
from socket import *
from _thread import *
import time
import sys

#aqui crearemos las funciones enunciadas en los comentarios y como se desarrollan

def ini():
    host = input("SERVIDOR :")
    port = int(input("Puerto: "))
    return host,port


def crearSocket():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def ligarSocket(s,host,port):
    while True:
        try:
            s.brind((host,port))
            break
        except error as e:
            print("ERROR", e)

def conexiones(s):
    conn,addr = s.accept()
    print("\n Conexión Establecida. \n El cliente es: ", addr[0] + ": ") + str(addr[1]+"\n")
    return conn,addr


def enviar(conn):
    msg = input("")
    msg = "Servidor: " + msg
    try:
        conn.send(msg.encode("UFT-8"))
    except:
        print("\n Algo ha pasado...")
        print("Intentalo en ")
        time.sleep(5)


def enviar2(conn):
    msg = input("")
    msg = "Servidor: " + msg
    try:
        conn.send(msg.encode("UTF-8"))

    except:
        print()
        print("\n Intentelo en 5 segundos \n")
        time.sleep(5)


def recibir(conn):
    while True:
        global  bandera
        try:
            reply = conn.recv(2048)
            reply = reply.decode("UFT-8")
            if reply[0] == "1":
                print("Cliente",reply)
                start_new_thread(enviar,(conn))
            elif reply[0] == "2":
                print("Cliente",reply)
                start_new_thread(enviar,(conn))
            else:
                Lista_de_clientes.append(reply[4])
                print("\n El cliente " + reply[4] + "Se ha ido")
                bandera = True
                break
        except:
            print("\n No puede recibirse repuesta")
            print("Intentelo en 5 segundos \n")
            time.sleep(5)


def enviarEspacial(conn):
    global Lista_de_clientes, client
    client = Lista_de_clientes.pop()
    conn.send(client.encode("UFT-8"))



#desde aca se usa variables globales

bandera = False # esta variable es utilizada en la conexion o desconexion de los clientes
Lista_de_clientes = ["2","1"] #esta linea del servidor coloca un numero a los clientes segun la llegada de ellos
client = ""  # esta variable se muestra el numero del cliente

#aqui vamos a crear nuestra funcion principal o tambien lalmada MAIN

def main():
    global  bandera
    host,port = ini()
    s = crearSocket()
    ligarSocket(s,host,port)
    s.listen(2)

    print("\n ADVERTENCIA: ESTE SERVIDOR ES TIPO ESCLAVO. EL NO"
           "ESCRIBE SI EL SERVIDOR NO TIENE NINGUN MENSAJE PARA RESPONDER")

    print("\n Esperamos por los clientes")

    conn, addr = conexiones(s)
    enviarEspacial(conn)
    start_new_thread(recibir(conn,))


    conn2, addr2 = conexiones(s)
    enviarEspacial(conn2)
    start_new_thread(recibir,(conn2,))

    while True:
        if bandera != True:
            conn3, addr3 = conexiones(s)
            enviarEspacial(conn3)
            start_new_thread(recibir,(conn3,))
            bandera = False



main()
