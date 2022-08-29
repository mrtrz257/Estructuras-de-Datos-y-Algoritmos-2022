import numpy as np

class ColaSec:
    __arreglo = None
    __max =  0
    __pr = 0
    __ul = 0
    __cantidad = 0
    def __init__(self, max = 0):
        self.__arreglo = np.empty(self.__max, dtype=int)
        self.__max = max
        self.__pr = 0
        self.__ul = 0
        self.__cantidad = 0
    def vacia(self):
        return self.__cantidad == 0
    def insertar(self, x):
        if self.__cantidad<self.__max:
            self.__arreglo[self.__ul]=x
            self.__ul = (self.__ul+1) % self.__max
            self.__cantidad += 1
            return x
        else:
            return 0
    def suprimir(self):
        if self.vacia():
            print("Pila Vacia")
            return -1
        else:
            x = self.__arreglo[self.__pr]
            self.__pr = (self.__pr+1) % self.__max
            self.__cantidad -= 1
            return x
    def recorrer(self):
        lista = []
        if not self.vacia():
            for i in range(self.__cantidad):
                elemento = self.suprimir()
                if elemento != -1:
                    lista.append(elemento)
        return lista
    def getCantidad(self):
        return self.__cantidad
    