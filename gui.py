#-*- coding: utf-8-*-

import server
import threading
from threading import Thread
from tkinter import *
import time
import progra_2
import tkinter.messagebox

 
def MandarPlantilla():
    #Mandar la plantilla al servidor solo si cliente es J1
    #Y formatearla en string y bytes
    plantilla = progra_2.main.lista.copy()
    plantillaMatriz = "|"

    for cuadro in plantilla:           
        objeto = str(cuadro.mina) + ","
        plantillaMatriz+= objeto

    plantillaMatriz+= "|"

    cliente.plantilla = plantillaMatriz
 
def eval(valor, obj):
    
    """
    esta funcion serÃ¡ para hacer cambios al hacer
    click excepto los cambios de boton
    (cambios multijugador) 
    (aqui es donde se hara cambios de todo lo que viene del server)

    """

    global total , totalminas, multi_offline, jugador1_local, jugador1_mult, puntos2, puntos

    try:
        #print(puntos2,"cececwc")
        pass
    except:
        #print("no existe")
        pass
    if not progra_2.main.perdio and conectados:
        perdiendo = [["Noob", "Por lo menos sabes jugar?"], ["Noob", "Jugando como nunca, pierde como siempre"], ["Noob", "Mejor dediquese a candy crush"]]

        if total == 1 and valor > 0 and not multi_offline:
          
            for x in listaMinasObjetos:
                if x.cuadro == obj:
                    fgColor = x.color()#
                    x.cuadro = Button(mainFrame, text=valor, fg=fgColor, bg="#8b8d8e", width=1, height=1)
                    x.cuadro.grid(row=x.x, column=x.y)
            tkinter.messagebox.showinfo("Ganaste", "Dale en una dificultad mas dificil :3")
      
        else:
            if valor == -1:
                try:
                    if not multi_online:

                        if jugador1_local or jugador1_mult :
                            
                            puntos+=1
                            print("si pasa por aqui_1", puntos)
                            if puntos > totalminas:
                                    tkinter.messagebox.showinfo("Se acabo","jugador 1 gano")            
                       
                        else:
                            puntos2 +=1
                            if puntos2 > totalminas:
                                tkinter.messagebox.showinfo("Se acabo","Jugador 2 gano")            
                        if puntos + puntos2 == total * 2:
                            tkinter.messagebox.showinfo("Se acabo","Empate")
                    else:
                        if J2:
                            puntos2+=1
                            if puntos2 > totalminas:
                                tkinter.messagebox.showinfo("Se acabo","Jugador 2 gano")            
                        else:
                            puntos+=1
                            if puntos > totalminas:
                                tkinter.messagebox.showinfo("Se acabo","Jugador 1 gano")            

                        
                except:
                    
                    progra_2.main.perdio = True
                    a = progra_2.choice(perdiendo)
                    tkinter.messagebox.showinfo(a[0], a[1])
                #Algoritmo de cliente a server
                try:#Dentro de try por si el jugador no escogio online esos variables no
                    #estan declarados
                    #Iteracion para buscar en cual mina le dio click el cliente para
                    #Para mandarlo al server
                    for indice in listaMinasObjetos:
                        if indice.cuadro == obj:
                            pos_indice = str(listaMinasObjetos.index(indice))
                            break
                    cliente.mandarMSG(str(puntos2 if J2 else puntos),pos_indice)
                    print(cliente.info)
                except:
                    pass
                      
            elif valor > 0:
                #Algoritmo de cliente a server
                 try:#Dentro de try por si el jugador no escojio online esos variables no
                    #estan declarados
                    #Iteracion para buscar en cual mina le dio click el cliente para
                    #Para mandarlo al server
                     for indice in listaMinasObjetos:
                        if indice.cuadro == obj:
                            pos_indice = str(listaMinasObjetos.index(indice))
                            break
                     cliente.mandarMSG(str(puntos2 if J2 else puntos),pos_indice)
                     print(cliente.info)
                 except:
                     pass
                 total -= 1
                 for x in listaMinasObjetos:
                     if x.cuadro == obj:
                         fgColor = x.color()
                         x.cuadro = Button(mainFrame, text=valor, fg=fgColor, bg="#8b8d8e", width=1, height=1)
                         x.cuadro.grid(row=x.x, column=x.y)

            elif not valor:
                total -= 1
 
                 #Algoritmo de cliente a server
                try:#Dentro de try por si el jugador no escojio online esos variables no
                     #estan declarados
                     #Iteracion para buscar en cual mina le dio click el cliente para
                     #Para mandarlo al server
                    for indice in listaMinasObjetos:
                        if indice.cuadro == obj:
                            pos_indice = str(listaMinasObjetos.index(indice))
                            break
                    cliente.mandarMSG(str(puntos2 if J2 else puntos),pos_indice)
                    print(cliente.info)
                except:
                    pass
                for x in listaMinasObjetos:
                    if x.cuadro == obj:
                        x.cuadro = Button(mainFrame, fg="black",
                                          bg="#a6a7a8", width=1, height=1)
                        x.cuadro.grid(row=x.x, column=x.y)
                for y in obj.coordenadas_alrededor:
                        coordenada = obj.x + y[0] * progra_2.main.largo + y[1]
                        if not progra_2.main.lista[coordenada].activo:
                            s = progra_2.main.lista[coordenada].click(True)
                            eval(s, progra_2.main.lista[coordenada])
def definir_puntos():
    global puntos, puntos2
    """
    Funcione que debe correr en
    un thread para conseguir en tiempo
    real los puntos del oponente mediante
    la comunicacion con el servidor
    """
    while True:
        time.sleep(0.07)
        #Cambiar los puntos del oponente
        try:#Dentro de try porque al inicio cliente.info es None
            if J2:
                puntos = cliente.info[0]
            else:
                puntos2 = cliente.info[0]
                if puntos2 == "200" or data[0] == "|":
                    puntos2 = 0
        except:pass

def demostrar(obj, izquierdo = True): 
    """
    obj es un objeto de listaminasobjetos
    esta funcion sera para cambiar el tipo de boton cada vez que da click
    """
    #print(222)
    global multi_offline, jugador1_local, jugador1_mult, multi_online, minasLabel
    if not progra_2.main.perdio:
        if not izquierdo  and (multi_online or multi_offline):
            return
        try:
            jugador1_local = not jugador1_local
        except:
            pass
        if izquierdo:
            valorDelClick = obj.cuadro.click(True)
        else:
            #print(obj.cuadro,"gg ixxi")
            valorDelClick  = progra_2.main.lista[progra_2.main.lista.index(obj.cuadro)].click(False)
        """
        ##print(multi_offline, "validando")

        print(izquierdo, "i" )
        """

        if obj.mina and izquierdo:#para poner
            #print(obj.mina, "validando")
            if multi_offline or multi_online:
                progra_2.main.lista[progra_2.main.lista.index(obj.cuadro)].click(True)
                obj.boton = Label(mainFrame, image=minaPNG)
                obj.boton.grid(row=obj.x, column=obj.y)
            else:       
                for par in listaMinasObjetos:
                    if par.mina:
                        print("cececcec")
                        progra_2.main.lista[progra_2.main.lista.index(par.cuadro)].click(True)
                        par.boton = Label(mainFrame, image=minaPNG)
                        par.boton.grid(row=par.x, column=par.y)
        
        elif obj.cuadro.bandera :
            obj.boton.grid_remove()
            minasLabel.destroy()
            progra_2.main.minas -= 1 
            minasLabel = Label(topMainFrame, text=progra_2.main.minas, bg="black", fg="red", width=30)
            minasLabel.grid(row=0, column=0, sticky="W")
            print("gg no llego")
            obj.boton = Button(mainFrame, image = banderaPNG)

            obj.boton.grid(row=obj.x, column=obj.y)

            obj.boton.bind("<Button-1>", lambda x: demostrar(obj))
            
            obj.boton.bind("<Button-3>", lambda x: demostrar(obj, False))                    

        elif not obj.cuadro.bandera and not izquierdo:
            print(222)
            minasLabel.destroy()
            progra_2.main.minas += 1 
            minasLabel = Label(topMainFrame, text=progra_2.main.minas, bg="black", fg="red", width=30)
            minasLabel.grid(row=0, column=0, sticky="W")
            obj.boton.grid_remove()
            obj.boton = Button(mainFrame, width=1,height=1, bg="#8b8d8e")

            obj.boton.grid(row=obj.x, column=obj.y)
            obj.boton.bind("<Button-1>", lambda x: demostrar(obj))
        
            obj.boton.bind("<Button-3>", lambda x: demostrar(obj, False))
        
        
        # if not obj.bandera:
        #           print("si funciona")
        #           progra_2.main.lista[progra_2.main.lista.index(par.cuadro)].click(True)
        #           par.boton = Label(mainFrame, image=banderaPNG, bg = "black")
        #           par.boton.grid(row=par.x, column=par.y)
        eval(valorDelClick, obj.cuadro)
    
    
   
class minasGUI:

    def __init__(self, boton, cuad, x, y, mina):
        self.x = x
        self.y = y
        self.boton = boton
        self.cuadro = cuad
        self.mina = mina
    
    
    def setupObj(self):

        self.boton.bind("<Button-1>", lambda x: demostrar(self))

        self.boton.grid(row=self.x, column=self.y)
        self.boton.bind("<Button-3>", lambda x: demostrar(self, False))

    def color(self):
        valores = {1: "#0000FF", 2: "#2d1a4f", 3: "#EF4321", 4: "#000000", 5: "#ba031f", 6: "#06ad91", 7: "#152959", 8: "#565759"}
        return valores[self.cuadro.minas_alrededor]


def revisar_coneccion():
   """
   Esta funcion va dentro de un thread
   revisa si hay coneccion al otro cliente
   para comenzar, en ese caso rompe el while
   """
   global conectados
   while True:
       
       
       data = cliente.info if cliente.info == None else cliente.info[0]
       
       if data == "200":
            conectados = True
            cliente.mandarMSG(cliente.plantilla)
            break

def puntos2Func():
    while True:
        Label(root, text=puntos2, fg="#800000", bg=mainBg, width=10).grid(row=1, column=2)
        time.sleep(0.5)

def puntos1Func():
    while True:
        Label(root, text=puntos, fg="#000080", bg=mainBg, width=10).grid(row=1, column=0)
        time.sleep(0.5)

def listo_minas(custom, dif, multParam=False , configuracion = {"reinicio" : False}):  # reinicio es para reiniciar true es que no a reinciado
    global listaMinasObjetos, mainFrame, cliente, \
           puntos, puntos2, jugador1_local, jugador1_mult, \
        totalminas, multi_online, multi_offline, topMainFrame, segundo,J2, conectados,textA,textL,textM
    segundo = 0
    progra_2.main.perdio = False
    multi_online = multParam
    topMainFrame = Frame(root)
    topMainFrame.grid(row=0,columnspan=3)
    topMainFrame.config(bg="black")



    mainFrame = Frame(root)
    mainFrame.grid(row=1, column=1)
       
    if not custom and not configuracion["reinicio"]:
        print("no debe pasar")
        textA, textM,textL = 0,0,0
    
    if not configuracion["reinicio"]: 
        if multi_offline or multi_online:
            #print("pero si llega")
            puntos, puntos2 = 0, 0 
            multi_offline = True
        else:
            multi_offline = False
        
        
        conectados = False if multi_online else True #Variable para saber si los clientes estan conectados
        if multi_online:
            cliente = server.Cliente("127.0.0.1")
            puntosThread = Thread(target=puntos1Func)
            puntosThread.daemon = True
            puntosThread.start()

            puntos2Thread = Thread(target=puntos2Func )
            puntos2Thread.daemon = True
            puntos2Thread.start()

            calcularPuntos = Thread(target=definir_puntos)
            calcularPuntos.daemon = True
            calcularPuntos.start()

            revisarCon = Thread(target=revisar_coneccion)
            revisarCon.daemon = True
            revisarCon.start()

            J2 = cliente.jugador
            conectados = True if J2 else False
            if conectados:
                print("un  si")
                cliente.mandarMSG("200")
            else:
                #print("minimo entra")
                #progra_2.main.ubicacion_online(cliente.plantilla)
                pass
        elif custom:
            if " " in textA.get() or " " in textL.get() or " " in textM.get():
                tkinter.messagebox.showwarning("Error", "no debes incluir espacios")
                return
            

            try:
                int(textA.get())
                int(textL.get())
                int(textM.get())

            except:
                tkinter.messagebox.showwarning("Error","Deben ser numeros enteros")
                return

            if int(textA.get()) < 3:
                tkinter.messagebox.showwarning("Error","Ancho debe ser mayor o igual a 3")
                return
            elif int(textA.get()) > 30:
                tkinter.messagebox.showwarning("Error", "Ancho debe ser menor o igual a 30")
                return

            elif int(textL.get()) < 3:
                tkinter.messagebox.showwarning("Error", "Largo debe ser mayor o igual a 3")
                return

            elif int(textL.get()) > 30:
                tkinter.messagebox.showwarning("Error", "Largo debe ser menor o igual a 30")
                return

            elif int(textM.get()) < 1:
                tkinter.messagebox.showwarning("Error", "Minas deben de ser mas que una")
                return

            elif int(textM.get()) > (int(textA.get())*int(textL.get()))-1:
                tkinter.messagebox.showwarning("Error", "Deben haber menos minas que cuadritos")
                return
            textA = int(textA.get())
            textL = int(textL.get())
            textM = int(textM.get())
            progra_2.main.ubicar_minas(0,ancho= textA,largo= textL,minas= textM)
            totalminas = textM // 2
        else:
            progra_2.main.ubicar_minas(dif)
            totalminas = progra_2.main.minas // 2
    else:
        detalle = configuracion["detalles"] 
        progra_2.main.ubicar_minas(detalle[0],ancho=detalle[1],largo = detalle[2], minas = detalle[3])
        totalminas = progra_2.main.minas // 2

    if  not multi_online:
        reiniciar = Label(topMainFrame,bg = "black", image=reiniciarIcon)
        reiniciar.grid(row=0,column=1)
        reiniciar.bind("<Button-1>", lambda x: main(reinicio = True ,detalles = [dif, textA, textL, textM]))
    else:
        if not J2:
            MandarPlantilla()
        else:
            pass
            #ConseguirPlantilla()

    global total, minasLabel
    total = progra_2.main.total - progra_2.main.minas
    minasLabel = Label(topMainFrame, text=progra_2.main.minas, bg="black", fg="red", width=30)
    minasLabel.grid(row=0, column=0, sticky="W")
    




    def tiempoFunc():
        # aux = 1
        # while True:
        #     if not aux:
        #       time.sleep(1)
        #     else:
        #       aux-=1
        #     try :
        #       tiempoLabel.destroy()
        #     except:
        #       pass
        global segundo, total
        segundo = 0
        while True:
            if progra_2.main.perdio:
                print("si cierra se imprime :v")
                sys.exit()
            
            try :
                #Este variable fondoTiempo se mantiene detras de tiempoLabel
                #para cuando se borre el tiempoLabel no haya un campo vacio
                fondoTiempo = Label(topMainFrame, bg="black", width=30)
                fondoTiempo.grid(row=0, column=2, sticky="E")
                tiempoLabel.destroy()
            except:pass
            tiempoLabel = Label(topMainFrame, text=int(segundo), bg="black", fg="red", width=30)
            tiempoLabel.grid(row=0, column=2, sticky="E")
            time.sleep(1)
            segundo += 1
            try:fondoTiempo.destroy()
            except:pass


    tfuncThread = Thread(target=tiempoFunc)
    tfuncThread.daemon = True
    if configuracion["reinicio"]:
         segundo =0

    elif not configuracion["reinicio"]:
         tfuncThread.start() 

    listaMinasObjetos = [] 
    for objeto in progra_2.main.lista:
             rowVar = progra_2.main.lista.index(objeto)//progra_2.main.largo#la fila
             columnVar = progra_2.main.lista.index(objeto)%progra_2.main.largo#la columna
             listaMinasObjetos.append(minasGUI(Button(mainFrame, width=1,height=1, bg="#8b8d8e"), objeto, rowVar, columnVar, objeto.mina) )
             listaMinasObjetos[-1].setupObj()
    try:
         containerCustom.destroy() 
    except:
         pass
    try:
        container.destroy()
    except:
        pass

    try:
         
        with open("temp") as temp:
            if temp:
                jugador1_mult = False
            else:
                jugador1_mult = True
            temp.close()
    except:
        pass
 
     


def pedirCustom(key):
    global textA, textL, textM, containerCustom, totalminas
    # tkinter.messagebox.showinfo("personalizado", "personalizado, por favor escriba las caracteristicas del juego")

    containerCustom = Frame(root)

    containerCustom.grid(row=1)

    textA = StringVar()
    labelAncho = Label(containerCustom, text="Ancho: ",
                       fg=mainFg, bg=mainBg, font=mainFont, width=mainWidth)
    entryAncho = Entry(containerCustom, textvariable=textA)
    textL = StringVar()
    labelLargo = Label(containerCustom, text="Largo: ",
                       fg=mainFg, bg=mainBg, font=mainFont, width=mainWidth)
    entryLargo = Entry(containerCustom, textvariable=textL)
    textM = StringVar()
    labelMinas = Label(containerCustom, text="Minas: ",
                       fg=mainFg, bg=mainBg, font=mainFont, width=mainWidth)
    entryMinas = Entry(containerCustom, textvariable=textM)

    readyButt = Button(containerCustom, text="Ok", fg=mainFg, bg=mainBg,
                       font=mainFont, width=mainWidth, command=lambda:  listo_minas(True, 0))
   
    readyButt.grid(row = 3, column = 0)
    labelAncho.grid(row = 0, column = 0)
    entryAncho.grid(row = 0, column = 1)
    labelLargo.grid(row = 1, column = 0)
    entryLargo.grid(row = 1, column = 1)
    labelMinas.grid(row = 2, column = 0)
    entryMinas.grid(row=2, column=1)


def Game(players , multiplayer, configuracion = {"reinicio" : False}):
    try :
        menuFrame.destroy()
    except:
        pass
    global container, multi_offline, multi_online

    
    if players:
        #print("pero si llega")
        global puntos2, puntos,jugador1_local
        puntos, puntos2, jugador1_local = 0, 0, False
        
        if multiplayer:
            multi_online = True
            multi_offline = False
        else:
            multi_online = False
            multi_offline = True
    else:
        multi_offline = False 
    if not configuracion["reinicio"]:
        container = Frame(root, bd=10, relief="groove")  
        container.config(bg="#8b8d8e")
            # Custom
        mode4Butt = Button(container, text="Custom", fg=mainFg,
                           bg=mainBg, font=mainFont, width=mainWidth)

        mode4Butt.bind("<Button-1>", pedirCustom)
        mode4Butt.grid(row=1, column=1)
        # 8x8
        mode1Butt = Button(container, text="8x8", fg=mainFg,
                           bg=mainBg, font=mainFont, width=mainWidth)
        # 16x16
        mode2Butt = Button(container, text="16x16", fg=mainFg,
                           bg=mainBg, font=mainFont, width=mainWidth)
        # 30x16
        mode3Butt = Button(container, text="30x16", fg=mainFg,
                           bg=mainBg, font=mainFont, width=mainWidth)


        mode3Butt.bind("<Button-1>", lambda x: listo_minas(False, 3, multiplayer))
        mode2Butt.bind("<Button-1>", lambda x: listo_minas(False, 2, multiplayer))
        mode1Butt.bind("<Button-1>", lambda x: listo_minas(False, 1, multiplayer))
 
        container.grid()
        mode1Butt.grid(row=0, column=0)
        mode2Butt.grid(row=0, column=1)
        mode3Butt.grid(row=1, column=0)
        
    else:
        listo_minas(0,configuracion["detalles"][0],False,configuracion)




def on_closing():
    #if tkinter.messagebox.askokcancel("Salir", "Enserio quieres salir :( ?"):
    try:cliente.sock.shutdown(server.socket.SHUT_RDWR)
    except:pass
    root.destroy()

def main(**configuracion):# confi =total mult, tamÃ±ao [1,2,4,5] , reinicio , reinicio va a ser False cuando es la primera llamada
    global root, mainFont, mainFg, mainBg, mainWidth, reiniciarIcon, menuFrame, minaPNG, banderaPNG
    try:
        root.destroy()
    except:
        pass

    root = Tk()
    root.title("Minesweeper")
    root.configure(background="#111111")
    root.protocol("WM_DELETE_WINDOW", on_closing)
    banderaPNG = PhotoImage(file ="./bandera.png")
    banderaPNG = banderaPNG.zoom(23)
    banderaPNG = banderaPNG.subsample(500)
    mainFont = ("Times", 11, "bold")
    mainFg = "black"
    mainBg = "#FFFFFF"
    mainWidth = 16  # ancho de botonbes
    minaPNG = PhotoImage(file="./mina.png")                                     
    minaPNG = minaPNG.zoom(28)
    minaPNG = minaPNG.subsample(450)
    reiniciarIcon = PhotoImage(file="./reiniciar.png")
    reiniciarIcon = reiniciarIcon.zoom(1)
    reiniciarIcon = reiniciarIcon.subsample(20)
    if not configuracion["reinicio"]:
        menuFrame = Frame(root, bd=10, relief="groove")
       
        OnePlayerL = Button(menuFrame, width=mainWidth, text="1-Player",
                            fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(0, False))
        TwoPlayerL = Button(menuFrame, width=mainWidth, text="2-Player",
                            fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(1, False))
        TwoPlayerM = Button(menuFrame, width=mainWidth, text="2-Player \nMultiplayer",
                           fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(1, True))                  
       
        menuFrame.grid(row=0, column=2, sticky="E")
        OnePlayerL.grid(row=0, column=0)
        TwoPlayerL.grid(row=1, column=0)
        TwoPlayerM.grid(row=2, column=0)
    else:
         Game(0,False,configuracion)
    root.mainloop()
 
if __name__ == "__main__":
    main(reinicio = False)
 
