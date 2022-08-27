import numpy as np

class Pila:
    __arreglo = None
    __cant = None
    __tope = None
    def __init__(self, cantidad = 0):
        self.__arreglo = np.empty(cantidad, dtype=int)
        self.__cant = cantidad
        self.__tope = -1
    def vacia(self):
        return self.__tope==-1
    def insertar(self, x):
        if self.__tope<self.__cant-1:
            self.__tope += 1
            self.__arreglo[self.__tope] = x
            return x
        else:
            return 0
    def suprimir(self):
        if self.vacia():
            print("Pila Vacia")
            return 0
        else:
            x = self.__arreglo[self.__tope]
            np.delete(self.__arreglo, self.__tope)
            self.__tope -= 1
            return x
    def mostrar(self):
        lista = []
        if not self.vacia():
            i = 0
            tope = self.__tope
            while i <= tope:
                elemento = self.suprimir()
                if elemento != 1:
                    lista.append(elemento)
                i += 1
        return lista
    def getTope(self):
        return self.__tope
    def getDatoTope(self):
        return self.__arreglo[self.__tope]
    def getCant(self):
        return self.__cant
    def mostrarArreglo(self):
        print(self.__arreglo)
