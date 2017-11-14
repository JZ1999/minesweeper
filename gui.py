import server
import threading
from threading import Thread
import time
from tkinter import *
import progra_2
import tkinter.messagebox

listaMinasObjetos = []  # Contiene listas de cada cuadrito y su botón respectivo


def color(num):
    valores = {1: "blue", 2: "#2d1a4f", 3: "#EF4321", 4: "#000000", 5: "#ba031f", 6: "#06ad91", 7: "#152959", 8: "#565759"}
    return valores[num]


def eval(valor, obj):
    global total

    perdiendo = [["Noob", "Por lo menos sabes jugar?"], ["noob", "jugando como nunca, pierde como siempre"], ["noob", "mejor dediquese a candy crush"]]
    if total == 1 and valor >= 0:
    	for x in listaMinasObjetos:
            if x.cuadro == obj:
                fgColor = color(valor)
                x.cuadro = Button(mainFrame, text=valor, fg=fgColor, bg="#8b8d8e", width=1, height=1)
                x.cuadro.grid(row=x.x, column=x.y)
    	#tkinter.messagebox.showinfo("ganaste", "perfecto")
    else:
        if valor == -5:
            pass
        if valor == -1:
            a = progra_2.choice(perdiendo)
            #tkinter.messagebox.showinfo(a[0], a[1])
        elif valor in [1, 2, 3, 4, 5, 6, 7, 8]:
            total -= 1
            for x in listaMinasObjetos:
                if x.cuadro == obj:
                    fgColor = color(valor)
                    x.cuadro = Button(
                        mainFrame, text=valor, fg=fgColor, bg="#8b8d8e", width=1, height=1)
                    x.cuadro.grid(row=x.x, column=x.y)
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
    


def demostrar(obj, x, y):
	valorDelClick = progra_2.main.lista[progra_2.main.lista.index(obj)].click(True)
	if obj.mina:
		for par in listaMinasObjetos:
			if par.cuadro == obj:
				progra_2.main.lista[progra_2.main.lista.index(par.cuadro)].click(True)
				par.boton = Label(mainFrame, image=minaPNG)
				par.boton.grid(row=x, column=y)
	eval(valorDelClick, obj)
	


class minasGUI:

    def __init__(self, boton, cuadro, x, y):
        self.x = x
        self.y = y
        self.boton = boton
        self.cuadro = cuadro

    def setupObj(self):

        self.boton.bind("<Button-1>", lambda x: demostrar(self.cuadro,self.x, self.y))
        self.boton.grid(row=self.x, column=self.y)


def listo_minas(custom, dif, mult=False):  # valor es para reiniciar
    global listaMinasObjetos, mainFrame

    iniTime = int(time.time())
    mainFrame = Frame(root)
    mainFrame.grid(row=1)
    topMainFrame = Frame(root)
    topMainFrame.grid(row=0)
    topMainFrame.config(bg="black")
    if mult:
        cliente = server.Cliente("127.0.0.1")
    if custom and valor:
        if " " in textA.get() or " " in textL.get() or " " in textM.get():
            tkinter.messagebox.showwarning(
                "Error", "no debes incluir espacios")
            return
        try:
            int(textA.get())
            int(textL.get())
            int(textM.get())
        except:
            tkinter.messagebox.showwarning("Error","Deben ser numeros y enteros")
            return

        if int(textA.get()) < 3:
            tkinter.messagebox.showwarning("Error","Ancho debe ser mayor o igual a 3")
            return
        elif int(textA.get()) > 15:
            tkinter.messagebox.showwarning("Error", "Ancho debe ser menor o igual a 15")
            return
        elif int(textL.get()) < 3:
            tkinter.messagebox.showwarning("Error", "Largo debe ser mayor o igual a 3")
            return
        elif int(textL.get()) > 15:
            tkinter.messagebox.showwarning("Error", "Largo debe ser menor o igual a 15")
            return
        elif int(textM.get()) < 1:
            tkinter.messagebox.showwarning("Error", "Minas deben de ser mas que una")
            return
        elif int(textM.get()) > (int(textA.get())*int(textL.get()))-1:
            tkinter.messagebox.showwarning("Error", "Deben haber menos minas que cuadritos")
            return
        
        progra_2.main.ubicar_minas(0,ancho= int(textA.get()),largo=int(textL.get()),minas=int(textM.get()))

        

    else:
        progra_2.main.ubicar_minas(dif)
    reiniciar = Label(topMainFrame,bg = "black", image=reiniciarIcon)
    global total
    total = progra_2.main.total - progra_2.main.minas
    reiniciar.grid(row=0,column=1)
    reiniciar.bind("<Button-1>", lambda x: listo_minas(custom, dif))
    minasLabel = Label(topMainFrame, text=20, bg="black", fg="red", width=30)
    minasLabel.grid(row=0, column=0, sticky="W")
    #aqui es el error de la caja al tkintear el miner


    def tiempoFunc():
        aux = 1
        while True:
            if not aux:time.sleep(1)
            else:aux-=1
            try:tiempoLabel.destroy()
            except:
                pass
            tiempoLabel = Label(topMainFrame, text=int(time.time())-iniTime, bg="black", fg="red", width=30)
            tiempoThread = Thread(target = tiempoLabel.grid(row=0, column=2, sticky="E" ))
            tiempoThread.daemon = True
            tiempoThread.start()
            #tiempo.grid(row=0, column=2, sticky="E")

    tfuncThread = Thread(target=tiempoFunc)
    tfuncThread.daemon = True
    tfuncThread.start()
    for objeto in progra_2.main.lista:
             rowVar = progra_2.main.lista.index(objeto)//progra_2.main.largo#la fila
             columnVar = progra_2.main.lista.index(objeto)%progra_2.main.largo#la columna
             #print(rowVar)
             listaMinasObjetos.append(minasGUI(Button(mainFrame, width=1,height=1, bg="#8b8d8e"), objeto, rowVar, columnVar) )

             #listaMinasObjetos[-1].boton.bind("<Button-1>",lambda x: demostrar(objeto))
             listaMinasObjetos[-1].setupObj()
             #listaMinasObjetos[-1].boton.grid(row=rowVar, column=columnVar)
    try:
         containerCustom.destroy() 
    except:
         pass
    container.destroy()

def pedirCustom(key):
    global textA, textL, textM, containerCustom
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


def Game(players, multiplayer):
    menuFrame.destroy()
    global container
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
    mode3Butt.bind("<Button-1>", lambda x: listo_minas(False, 3))
    mode2Butt.bind("<Button-1>", lambda x: listo_minas(False, 2))
    mode1Butt.bind("<Button-1>", lambda x: listo_minas(False, 1, True))

    container.grid()
    mode1Butt.grid(row=0, column=0)
    mode2Butt.grid(row=0, column=1)
    mode3Butt.grid(row=1, column=0)
    mode4Butt.grid(row=1, column=1)

root = Tk()

root.title("Minesweeper")
root.configure(background="#111111")
root.geometry("600x600")
mainFont = ("Times", 11, "bold")
mainFg = "black"
mainBg = "#FFFFFF"
mainWidth = 16  # ancho de botones
menuFrame = Frame(root, bd=10, relief="groove")
OnePlayerL = Button(menuFrame, width=mainWidth, text="1-Player",
                    fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(1, False))
TwoPlayerL = Button(menuFrame, width=mainWidth, text="2-Player",
                    fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(2, False))
TwoPlayerM = Button(menuFrame, width=mainWidth, text="2-Player \nMultiplayer",
                    fg=mainFg, bg=mainBg, font=mainFont, command=lambda: Game(2, True))
minaPNG = PhotoImage(file="./mina.png")
minaPNG = minaPNG.zoom(28)
minaPNG = minaPNG.subsample(389)
reiniciarIcon = PhotoImage(file="./reiniciar.png")
reiniciarIcon = reiniciarIcon.zoom(1)
reiniciarIcon = reiniciarIcon.subsample(20)

menuFrame.grid(row=0, column=2, sticky="E")
OnePlayerL.grid(row=0, column=0)
TwoPlayerL.grid(row=1, column=0)
TwoPlayerM.grid(row=2, column=0)


root.mainloop()
