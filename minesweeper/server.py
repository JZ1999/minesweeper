import os
import time
import threading
import socket
import sys

class Servidor:
	#primer parametro es que usaremos IPV4, 2do es para decir usaremos una coneccion TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        def __init__(self):
		#primer parametro es el IP que le quiere poner al sock, segundo es el puerto
                self.sock.bind(('127.0.0.1', 9999))

		#Abilita las conecciones con el parametro diciendo cuantas conecciones deja
                self.sock.listen(1)

	#Lista donde tendremos todas las conecciones
        conecciones = []
        
        def manejo(self, c, a):
            while True:
                #recv es la informacion que se recive de la coneccion, 1024 es el maximo de informacion que se puede recibir en bytes
                data = c[0].recv(1024)
                for self.coneccion in self.conecciones:
                    #mandandole data en bytes a coneccion
                    if c[0] != self.coneccion[0]:
                        self.coneccion[0].send(bytes(data))
                if not data:
                    print(str(a[0])+":"+str(a[1])+" desconectado ID: "+c[1])
                    self.conecciones.remove(c)
                    c[0].close()
                    break
        def correr(self): 
            id = 0
            while True:
                
                #if not id:
                #    os.remove("temp")
                id+=1
                # c = coneccion, a = address
                c, a = self.sock.accept()
                #creando una variable en la clase de c de ID
                c = (c,str(id))
                #El thread se ocupa para tener mas que una coneccion a la misma vez
                #target = funcion que se aplicara con lo que retorna el método de Thread, args = los parametros de la funcion de target
                cThread = threading.Thread(target=self.manejo, args=(c, a))
                #daemon en True nos deja cerrar todos los threads sin que el OS nos de problemas al cerrar el programa
                cThread.daemon = True
                #Comienza el thread
                cThread.start()
                self.conecciones.append(c)
                with open("temp","a") as temp:
                    temp.write(str(c))
                    temp.close()
                print(str(a[0])+":"+str(a[1])+" conectado ID: "+c[1])


class Cliente:
    print("sea necio")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    info = None#Informacion que manda al server
    def mandarMSG(self, *args):
        self.sock.send(bytes(" ".join(args), "utf-8"))
        #time.sleep(0.5)
    def recibir(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data.decode("UTF-8"))
            info = (data.decode("UTF-8")).split(" ")
    def __init__(self, addr):
        self.sock.connect((addr, 9999))
        
        iThread = threading.Thread(target=self.mandarMSG)
        iThread.daemon = True
        #iThread.start()
        
        rThread = threading.Thread(target=self.recibir)
        rThread.daemon = True
        rThread.start()


if __name__ == "__main__":
    server = Servidor()
    server.correr()

