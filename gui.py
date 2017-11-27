#-*- coding: utf-8-*-
import server
import threading
from threading import Thread
from tkinter import *
import time
import progra_2
import tkinter.messagebox
listaMinasObjetos = []  # Contiene listas de cada cuadrito y su botón respectivo


def eval(valor, obj):
    
    """
    esta funcion será para hacer cambios al hacer
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
    if not progra_2.main.perdio:
        try:
            for indice in listaMinasObjetos:
                if indice.cuadro == obj:
                    pos_indice = str(listaMinasObjetos.index(indice))
                    break
            cliente.mandarMSG(str(puntos),pos_indice)
            print(cliente.info)
            #print(str(puntos),pos_indice)
        except:
            pass
        perdiendo = [["Noob", "Por lo menos sabes jugar?"], ["Noob", "Jugando como nunca, pierde como siempre"], ["Noob", "Mejor dediquese a candy crush"]]

        if total == 1 and valor > 0 and not multi_offline:
            print(200)

            for x in listaMinasObjetos:
                if x.cuadro == obj:
                    fgColor = x.color()#
                    x.cuadro = Button(mainFrame, text=valor, fg=fgColor, bg="#8b8d8e", width=1, height=1)
                    x.cuadro.grid(row=x.x, column=x.y)
            tkinter.messagebox.showinfo("Ganaste", "Dale en una dificultad mas dificil :3")
      
        else:
            if valor == -1:
                    try:

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
                            
                    except:
                        progra_2.main.perdio = True
                        a = progra_2.choice(perdiendo)
                        tkinter.messagebox.showinfo(a[0], a[1])
                      
            elif valor > 0:
                total -= 1
                for x in listaMinasObjetos:
                    if x.cuadro == obj:
                        fgColor = x.color()
                        x.cuadro = Button(mainFrame, text=valor, fg=fgColor, bg="#8b8d8e", width=1, height=1)
                        x.cuadro.grid(row=x.x, column=x.y)
            # elif valor == -3:
            #      for x in listaMinasObjetos:
            #          if x.cuadro == obj:
            #              x.cuadro = Button(mainFrame, fg="black",
            #                                bg="#555555", width=1, height=1)
            #              x.cuadro.grid(row=x.x, column=x.y)
            # elif valor == -2:
            #     obj.destroy()
            #     for x in listaMinasObjetos:
            #         if x.cuadro == obj:
            #             x.cuadro = Button(mainFrame, fg="blue",
            #                            bg="#a6a7a8", width=1, height=1)
            #             x.cuadro.grid(row=x.x, column=x.y)
            elif not valor:
                total -= 1

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

def demostrar(obj, izquierdo = True): 
	"""
	obj es un objeto de listaminasobjetos
	esta funcion sera para cambiar el tipo de boton cada vez que da click
	"""
	#print(222)
	global multi_offline, jugador1_local, jugador1_mult, multi_online, minasLabel
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
	# 			print("si funciona")
	# 			progra_2.main.lista[progra_2.main.lista.index(par.cuadro)].click(True)
	# 			par.boton = Label(mainFrame, image=banderaPNG, bg = "black")
	# 			par.boton.grid(row=par.x, column=par.y)
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

def reciba_puntos_Func(puntosParam):
    while True:
        recv = cliente.recibir()
        print(next(recv))

def puntos2Func():
    while True:
        Label(root, text=puntos2, fg="#800000", bg=mainBg, width=10).grid(row=1, column=2)
        time.sleep(0.5)

def puntos1Func():
    while True:
        Label(root, text=puntos, fg="#000080", bg=mainBg, width=10).grid(row=1, column=0)
        time.sleep(0.5)

def listo_minas(custom, dif, multParam=False ,reinicio= False):  # reinicio es para reiniciar true es que hay qeu reiniciar
    global listaMinasObjetos, mainFrame, cliente, \
           puntos, puntos2, jugador1_local, jugador1_mult, \
            totalminas, multi_online, multi_offline, topMainFrame, segundo,textA,textL,textM
    if not custom:
    	textA,textL,textM = 0,0,0

    segundo = 0
    progra_2.main.perdio = False
    multi_online = multParam
    
    if multi_offline or multi_online:
        #print("pero si llega")
        puntos, puntos2 = 0, 0 
        multi_offline = True
    else:
        multi_offline = False
    try:
            mainFrame.destroy()
    except:
        pass


    # recibapuntosThread = Thread(target=reciba_puntos_Func, args=(puntos2 if esJ1 else puntos2))
    # recibapuntosThread.daemon = True
    # recibapuntosThread.start()
    
    
    mainFrame = Frame(root)
    mainFrame.grid(row=1, column=1)
    topMainFrame = Frame(root)
    topMainFrame.grid(row=0,columnspan=3)
    topMainFrame.config(bg="black")
    
    if multi_online:
        cliente = server.Cliente("127.0.0.1")
        puntosThread = Thread(target=puntos1Func)
        puntosThread.daemon = True
        puntosThread.start()
        puntos2Thread = Thread(target=puntos2Func )
        puntos2Thread.daemon = True
        puntos2Thread.start()
    if not reinicio:
	    if custom:
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

	        progra_2.main.ubicar_minas(0,ancho= int(textA.get()),largo=int(textL.get()),minas=int(textM.get()))
	        totalminas = int(textM.get()) // 2
	   
	    else:
	        print("aqui solo entra si no es custom")
	        progra_2.main.ubicar_minas(dif)
	        totalminas = progra_2.main.minas // 2
    else:
        print("def",dif)
        progra_2.main.ubicar_minas(custom,ancho= int(dif[1]),largo= int(dif[2]),minas= int(dif[3]))
        totalminas = progra_2.main.minas // 2
    reiniciar = Label(topMainFrame,bg = "black", image=reiniciarIcon)
    global total, minasLabel
    total = progra_2.main.total - progra_2.main.minas
    reiniciar.grid(row=0,column=1)
    reiniciar.bind("<Button-1>", lambda x: main(reinicio = True, jugadores = jugador1_local, detalles = [dif, textA, textL, textM]))
    minasLabel = Label(topMainFrame, text=progra_2.main.minas, bg="black", fg="red", width=30)
    minasLabel.grid(row=0, column=0, sticky="W")
    print("progra_2.main.lista[0]", progra_2.main.lista[0])
    time.sleep(2)
    progra_2.main.lista[0].alrededor_mina()
        

    def tiempoFunc():
        # aux = 1
        # while True:
        #     if not aux:
        #     	time.sleep(1)
        #     else:
        #     	aux-=1
        #     try :
        #     	tiempoLabel.destroy()
        #     except:
        #     	pass
        global segundo
        while True:
            tiempoLabel = Label(topMainFrame, text=int(segundo), bg="black", fg="red", width=30)
            tiempoLabel.grid(row=0, column=2, sticky="E")
            time.sleep(1)
            segundo += 1


    tfuncThread = Thread(target=tiempoFunc)
    tfuncThread.daemon = True
    # if reinicio:
    # 	tfuncThread.start()  
    # else:
    #     pass
    
    for objeto in progra_2.main.lista:
             rowVar = progra_2.main.lista.index(objeto)//progra_2.main.largo#la fila
             columnVar = progra_2.main.lista.index(objeto)%progra_2.main.largo#la columna
             #print(rowVar)
             listaMinasObjetos.append(minasGUI(Button(mainFrame, width=1,height=1, bg="#8b8d8e"), objeto, rowVar, columnVar, objeto.mina) )
             #listaMinasObjetos[-1].boton.bind("<Button-1>",lambda x: demostrar(objeto))
             listaMinasObjetos[-1].setupObj()
             #listaMinasObjetos[-1].boton.grid(row=rowVar, column=columnVar)
    try:
         containerCustom.destroy() 
    except:
         pass
    container.destroy()

    with open("temp") as temp:
        if temp:
            jugador1_mult = False
        else:
            jugador1_mult = True
        temp.close()
    

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


def Game(players, multiplayer, reinicio = False, configuracion = None):
    try :
    	menuFrame.destroy()
    except:
    	pass
    global container, multi_offline,jugador1_local
    multi_offline = bool(players)
    jugador1_local = not bool(players)
    if players:
        #print("pero si llega")
        global puntos2, puntos
        puntos, puntos2  = 0, 0
        

    if not reinicio:

	    container = Frame(root, bd=10, relief="groove")  
	    container.config(bg="#8b8d8e")

	    # 8x8
	    mode1Butt = Button(container, text="8x8", fg=mainFg,
	                       bg=mainBg, font=mainFont, width=mainWidth)
	    # 16x16
	    mode2Butt = Button(container, text="16x16", fg=mainFg,
	                       bg=mainBg, font=mainFont, width=mainWidth)
	    # 30x16
	    mode3Butt = Button(container, text="30x16", fg=mainFg,
	                       bg=mainBg, font=mainFont, width=mainWidth)
	    # Custom
	    mode4Butt = Button(container, text="Custom", fg=mainFg,
	                       bg=mainBg, font=mainFont, width=mainWidth)
	    mode4Butt.bind("<Button-1>", pedirCustom)
	    mode3Butt.bind("<Button-1>", lambda x: listo_minas(False, 3, multiplayer))
	    mode2Butt.bind("<Button-1>", lambda x: listo_minas(False, 2, multiplayer))
	    mode1Butt.bind("<Button-1>", lambda x: listo_minas(False, 1, multiplayer))

	    container.grid()
	    mode1Butt.grid(row=0, column=0)
	    mode2Butt.grid(row=0, column=1)
	    mode3Butt.grid(row=1, column=0)
	    mode4Butt.grid(row=1, column=1)
    else:
    	listo_minas(False, configuracion["detalles"], False, True )
    
def on_closing():
    #if tkinter.messagebox.askokcancel("Salir", "Enserio quieres salir :( ?"):
    try:cliente.sock.shutdown(server.socket.SHUT_RDWR)
    except:pass
    root.destroy()

# root = Tk()
# root.title("Minesweeper")
# root.configure(background="#111111")
# root.geometry("600x600")

# #root.protocol("WM_DELETE_WINDOW", on_closing)
# mainFont = ("Times", 11, "bold")
# mainFg = "black"
# mainBg = "#FFFFFF"
# mainWidth = 16  # ancho de botones
# menuFrame = Frame(root, bd=10, relief="groove")
# OnePlayerL = Button(menuFrame, width=mainWidth, text="1-Player",
#                     fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(1, False))
# TwoPlayerL = Button(menuFrame, width=mainWidth, text="2-Player",
#                     fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(2, False))
# TwoPlayerM = Button(menuFrame, width=mainWidth, text="2-Player \nMultiplayer",
#                     fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(2, True))
# minaPNG = PhotoImage(file="./mina.png")
# minaPNG = minaPNG.zoom(28)
# minaPNG = minaPNG.subsample(389)
# banderaPNG = PhotoImage(file = "./bandera.png")
# banderaPNG = banderaPNG.zoom(28)
# banderaPNG = banderaPNG.subsample(390)
# reiniciarIcon = PhotoImage(file="./reiniciar.png")
# reiniciarIcon = reiniciarIcon.zoom(1)
# reiniciarIcon = reiniciarIcon.subsample(20)

# menuFrame.grid(row=0, column=2, sticky="E")
# OnePlayerL.grid(row=0, column=0)
# TwoPlayerL.grid(row=1, column=0)
# TwoPlayerM.grid(row=2, column=0)


# root.mainloop()
# =======
#         quit()

def main(**configuracion):# confi =total mult, tamñao [1,2,4,5] , reinicio , reinicio va a ser False cuando es la primera llamada
    global root, mainFont, mainFg, mainBg, mainWidth, reiniciarIcon, menuFrame, minaPNG, banderaPNG
    try:
    	root.destroy()
    except:
    	pass
# cantidad de jugadores,
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
        Game(configuracion["jugadores"],False ,True, configuracion)
    root.mainloop()

if __name__ == "__main__":
    main(reinicio = False)

