from Pila import Pila
import numpy as np

class Manejador:
    __cantidad = None
    __cont = 0
    __pilas = None
    def __init__(self, cantidad):
        self.__cantidad = cantidad
        self.__cont = 0
        self.__pilas = np.empty(3, dtype=Pila)
    def __str__(self):
        texto = ''
        for i in range(len(self.__pilas)):
            texto += self.Grafico(self.__pilas[i], i)
            texto += '\n////////////////////////////////////////////////////'
        return texto
    def Escaneo(self):
        cont = self.__pilas[2].mostrar()
        self.__pilas[2] = self.reLoad(cont)
        return cont
    def Grafico(self, pila, posicion):
        text = '\n|'
        disco = '-----'
        torre = pila
        contenido = torre.mostrar()
        cont = 0
        if (len(contenido) > 0):
                for elemento in contenido:
                    text += '\n|'
                    text += '\n' + (disco * elemento)
        else:
                for i in range(self.__cantidad):
                    text += '\n|\n|'
        text += '\n|'
        self.__pilas[posicion] = self.reLoad(contenido)
        return text
    def reLoad(self, contenido):
        contenido.sort(reverse=True)
        pila = Pila(self.__cantidad)
        for cont in contenido:
            pila.insertar(cont)
        return pila
    def cargarPila(self, pila):
        if (self.__cont < self.__cantidad):
            self.__pilas[self.__cont] = pila
            self.__cont += 1
    def moverTope(self, inicio, final):
        tope = self.__pilas[inicio-1].suprimir()
        self.__pilas[final-1].insertar(tope)
    def getTope(self, pos):
        return self.__pilas[pos-1].getTope()
    def getDatoTope(self, pos):
        return self.__pilas[pos-1].getDatoTope()
    def getLen(self):
        return len(self.__pilas)
