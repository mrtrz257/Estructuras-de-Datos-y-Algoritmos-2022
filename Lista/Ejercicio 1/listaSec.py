import numpy as np

class ListaSec:
    __arreglo = None
    __cantidad = None
    __ultimo = None
    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__ultimo = 0
    def crear(self):
        self.__arreglo = np.empty(self.__cantidad, dtype=int)
    def vacia(self):
        return self.__ultimo == 0
    def insertar(self, elemento, posicion):
        if posicion == self.__ultimo+1 and posicion < self.__cantidad-1:
            self.__arreglo[posicion] = elemento
        elif posicion < 0 and posicion<=self.__ultimo:
            if self.recuperar(posicion) == None:
                self.__arreglo[posicion] = elemento
            else:
                pass
                ######
    def suprimir(self, posicion):
        if posicion == self.__ultimo:
            self.__ultimo -= 1
        del self.__arreglo[posicion]
        ######
    def recuperar(self, posicion):
        if not self.vacia():
            return self.__arreglo[posicion]
    def ultimoElemento(self):
        if not self.vacia():
            return self.__arreglo[self.__ultimo]
        else:
            return None
    def primerElemento(self):
        if not self.vacia():
            return self.__arreglo[0]
        else:
            return None
    def siguiente(self, posicion):
        if not self.vacia():
            if self.recuperar[posicion]!=None:
                return self.__arreglo[posicion+1]
            ######        

    def anterior(self):
        pass
        ######

    def recorrer(self):
        if not self.vacia():
            for i in range(self.__cantidad):
                elemento = self.recuperar(i)
                print(elemento)
