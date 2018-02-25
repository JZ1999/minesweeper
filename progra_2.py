from random import *

class partida:
    def __init__(self):
        
        self.lista = []
        self.largo = 0
        self.minas = 0
        self.total = 0
        self.perdio = False

    def ubicacion_online(self, minas):
        if  len(minas) == 64:
            self.largo = 8
            self.minas = 10
        elif  len(minas) == 256:
            self.largo = 16
            self.minas = 40
        else:
            self.largo = 30
            self.minas = 99
        self.total = len(minas)

        lista =[[]] * self.total
        lista = list(map(lambda x: cuadro(x), minas))
        self.lista = lista

        self.lista[0].alrededor_mina()



    def ubicar_minas(self,dificultad, **customizado):  # creacion y ubicacion de la mina y lista, esto no va en esta class
        nivel = [[8, 8, 10], [16, 16, 40], [16, 30, 99]]
        
        print("debugenado" ,dificultad, customizado)
        if dificultad:
            print("debugenad1" ,dificultad, customizado)
            ancho, largo, minas = nivel[dificultad - 1][0], nivel[dificultad - 1][1], nivel[dificultad - 1][2]
        else:
            ancho = customizado["ancho"]
            largo = customizado["largo"]
            minas = customizado["minas"]
        self.largo = largo
        self.total = largo * ancho
        self.minas = minas
        lista = [[]] * (self.total)
        lista = list(map(lambda x: cuadro(), lista))# pichudisima
        for t in range(len(lista)):
            lista[t].x = t
        while minas:
            x = choice(lista)
            if not x.mina:
                lista[lista.index(x)].mina = True
                minas -= 1
        self.lista = lista
        self.lista[0].alrededor_mina()
        
class cuadro(partida):
    def __init__(self, minas = False):
        self.x = None
        self.activo =  False # si es True se muestra al usuario, independientemente si es bandera/ bomba / vacio o un numero
        self.bandera = False 
        self.mina = minas
        self.minas_alrededor = 0
        self.coordenadas_alrededor = [] # esta va a tener las instrucciones para ir a los vecinos del cuadro

        super().__init__()


    def alrededor_mina(self):
        arreglo = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for x in main.lista:
            coordenada = main.lista.index(x)
            alrededor = arreglo.copy()
            if coordenada >= len(main.lista) - main.largo:
                alrededor.pop()
                alrededor.pop()
                alrededor.pop()
            if coordenada < main.largo:
                alrededor.pop(0)
                alrededor.pop(0)
                alrededor.pop(0)
            if coordenada % main.largo == main.largo - 1:
                alrededor.remove([0, 1])
                try:
                    alrededor.remove([-1, 1])
                except:
                    pass
                try:
                    alrededor.remove([1, 1])
                except:
                    pass
            if not coordenada % main.largo:
                alrededor.remove([0, -1])
                try:
                    alrededor.remove([-1, -1])
                except:
                    pass
                try:
                    alrededor.remove([1, -1])
                except:
                    pass

            for y in alrededor:
                if main.lista[main.lista.index(x) + y[0] * main.largo + y[1]].mina:
                    main.lista[main.lista.index(x)].minas_alrededor += 1

            main.lista[main.lista.index(x)].coordenadas_alrededor = alrededor
    def click(self, click_izquierda):
        #derecho activa casilla
        #izquierdo pone bandera
        # retorna 0 si no tiene ni una mina alrededor y entonces se activa
        # retorna 1-8 y seran las minas que toene alrededor y se activa
        # retorna -1 si es una mina y se activa
        # retorna -5 si no hace nada y se queda la casilla igual
        # retorna -3 si hay que poner bandera y no se activa
        # retorna -2 si hayq ue quitar bandera, queda el cuadro normal y no se activa
        if click_izquierda:
            if not self.activo:
                if not self.bandera:
                    self.activo = True
                    if not self.mina:
                        if self.minas_alrededor:
                            return self.minas_alrededor
                        return 0#no tiene minas alrededor
                    return -1
                return -5
            return -5
        else:
            print(1)
            if not self.activo:
                print(self.bandera)
                self.bandera = not self.bandera
                print(self.bandera)
                if self.bandera:
                    return -3#pone bandera
                print(3)
                return -2#quita bandera
            return -5# la casilla esta activa, no puede poner bandera
main = partida()
