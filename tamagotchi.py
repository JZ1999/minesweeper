from tkinter import *
global hambre_1
import tamago
hambre_1 = "False"

def cambiar():
	global hambre_1
	Respaldo = hambre_1
	hambre_1 = not Respaldo
	
root = Tk()
root.title("Tamagotchi")
root.configure(background="#111111")
root.geometry("400x200")

h = StringVar()
hambre = Label(root, text="tiene hambre?: ",
                       fg="black", width= 13)
entryh = Entry(root, textvariable=h)
readyButt = Button(containerCustom, text="Ok", fg=mainFg, bg=mainBg,
                       font=mainFont, width=mainWidth, command=lambda: tamagotchi.listo(h,h,h))
 
readyButt.grid(row = 3, column = 0)
"""
h = StringVar()
hambre = Button(root, width = 14, text="tiene hambre? \n" + hambre_1, bg="#FFFFFF", command = lambda : cambiar())

"""
hambre.grid()
entryh.grid()

root.mainloop()
