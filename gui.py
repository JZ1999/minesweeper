from tkinter import *
import progra_2
import tkinter.messagebox
def demostrar():
    pass

def listoCustom():
        progra_2.main.ubicar_minas(0,ancho= int (textA.get()),largo=int(textL.get()),minas=int(textM.get()))
        mainFrame = Frame(root)
        mainFrame.grid()
        for objeto in progra_2.main.lista:
            posicion_y = progra_2.main.lista.index(objeto)//progra_2.main.largo
            posicion_x = progra_2.main.lista.index(objeto)%progra_2.main.largo
            if objeto.mina:
                minaButt = Button(mainFrame, width=2,height=2, bg="#FFFFFF")
                minaButt.grid(row=posicion_y, column=posicion_x)
                minaButt.bind("<Button-1>",demostrar)
            else:
                minaButt = Button(mainFrame, width=2,height=2, bg="#000000")
                minaButt.grid(row=posicion_y, column=posicion_x)

def pedirCustom(key):
    global textA,textL,textM
    #tkinter.messagebox.showinfo("personalizado", "personalizado, por favor escriba las caracteristicas del juego")

    containerCustom = Frame(root)
    containerCustom.grid(row=1)

    textA = StringVar()
    labelAncho = Label(containerCustom, text = "Ancho: ", fg = mainFg, bg = mainBg, font = mainFont, width = mainWidth)
    entryAncho = Entry(containerCustom, textvariable = textA)
    textL = StringVar()
    labelLargo = Label(containerCustom, text = "Largo: ", fg = mainFg, bg = mainBg, font=mainFont, width = mainWidth)
    entryLargo = Entry(containerCustom, textvariable = textL)
    textM = StringVar()
    labelMinas = Label(containerCustom, text = "Minas: ", fg = mainFg, bg = mainBg, font = mainFont, width = mainWidth)
    entryMinas = Entry(containerCustom, textvariable=textM)

    readyButt = Button(containerCustom, text = "Ok", fg = mainFg, bg = mainBg, font = mainFont, width = mainWidth, command = listoCustom)

    readyButt.grid(row = 3, column = 0)
    labelAncho.grid(row = 0, column = 0)
    entryAncho.grid(row = 0, column = 1)
    labelLargo.grid(row = 1, column = 0)
    entryLargo.grid(row = 1, column = 1)
    labelMinas.grid(row = 2, column = 0)
    entryMinas.grid(row = 2, column = 1)

   

def Game(players, multiplayer):
    menuFrame.destroy()
    container = Frame(root, bd=10, relief="groove")# freme kja :v

    #8x8
    mode1Butt = Button(container, text = "8x8", fg = mainFg,bg = mainBg, font = mainFont, width = mainWidth, command= lambda: progra_2.main.ubicar_minas(1))
    #16x16
    mode2Butt = Button(container, text="16x16", fg=mainFg,bg=mainBg,font = mainFont, width = mainWidth, command= lambda: progra_2.main.ubicar_minas(2))
    #30x16
    mode3Butt = Button(container, text="30x16", fg=mainFg,bg=mainBg,font=mainFont,width=mainWidth, command= lambda: progra_2.main.ubicar_minas(3))
    #Custom
    mode4Butt = Button(container, text="Custom", fg=mainFg,bg=mainBg,font=mainFont,width=mainWidth)

    mode4Butt.bind("<Button-1>", pedirCustom)


    container.grid()
    mode1Butt.grid(row=0,column=0)
    mode2Butt.grid(row=0,column=1)
    mode3Butt.grid(row=1,column=0)
    mode4Butt.grid(row=1,column=1)

root = Tk()

root.title("Minesweeper")
root.configure(background="#555555")
#root.geometry("400x400")
mainFont = ("Times", 11, "bold")
mainFg = "black"
mainBg = "#FFFFFF"
mainWidth = 16 #ancho de botones
menuFrame = Frame(root, bd = 10, relief="groove")
OnePlayerL = Button(menuFrame, width=mainWidth,text="1-Player",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(1,False))
TwoPlayerL = Button(menuFrame, width=mainWidth,text="2-Player",fg= mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,False))
TwoPlayerM = Button(menuFrame, width=mainWidth,text="2-Player \nMultiplayer",fg=mainFg,bg=mainBg,font=mainFont,command=lambda: Game(2,True))

menuFrame.grid(row=0,column=2,sticky="E")
OnePlayerL.grid(row=0,column=0)
TwoPlayerL.grid(row=1,column=0)
TwoPlayerM.grid(row=2,column=0)


root.mainloop()
