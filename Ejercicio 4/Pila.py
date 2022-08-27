import numpy as np

class Pila:
    __arreglo = None
    __cant = None
    __tope1 = None
    __tope2 = None
    def __init__(self, cantidad = 0):
        self.__arreglo = np.empty(cantidad, dtype=int)
        self.__cant = cantidad
        self.__tope1 = -1
        self.__tope2 = cantidad
    def vacia1(self):
        return self.__tope1==-1
    def vacia2(self):
        return self.__tope2==self.__cant+1
    def insertar1(self, x):
        if self.__tope1<self.__tope2-1:
            self.__tope1 += 1
            self.__arreglo[self.__tope1] = x
            return x
        else:
            return 0
    def insertar2(self, x):
        if self.__tope2>self.__tope1+1:
            self.__tope2 -= 1
            self.__arreglo[self.__tope2] = x
            return x
        else:
            return 0
    def suprimir1(self):
        if self.vacia1():
            print("Pila 1 Vacia")
            return -1
        else:
            x = self.__arreglo[self.__tope1]
            self.__tope1 -= 1
            return x
    def suprimir2(self):
        if self.vacia2():
            print("Pila 2 Vacia")
            return -1
        else:
            x = self.__arreglo[self.__tope2]
            self.__tope2 += 1
            return x
    def mostrar1(self):
        if not self.vacia1():
            i = 0
            tope = self.__tope1
            while i <= tope:
                elemento = self.suprimir1()
                if elemento != -1:
                    print(elemento)
                i += 1
    def mostrar2(self):
        if not self.vacia2():
            i = self.__cant - 1
            tope = self.__tope2
            while i >= tope:
                elemento = self.suprimir2()
                if elemento != -1:
                    print(elemento)
                i -= 1
