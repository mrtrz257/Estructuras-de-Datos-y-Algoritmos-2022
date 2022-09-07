import numpy as np

from Nodo import Nodo

class Lista:
    __arreglo = None
    __primerL = None
    __primerD = None
    __cant = None

    def __init__(self, cant=0):
        self.__arreglo = np.empty(cant, dtype=Nodo)
        self.incializacion()
        self.__primerL = -1
        self.__primerD = 0
        self.__cant = 0
    def incializacion(self):
        print('ENTRA')
        for i in range(len(self.__arreglo)):
            nodo = Nodo(0)
            if (i == 0):
                self.__arreglo[i] = nodo
            else:
                self.__arreglo[i] = nodo
                self.__arreglo[i - 1].setSiguiente(i)
    def vacia(self):
        return self.__primerL == -1
    def primerElemento(self):
        return self.__arreglo[self.__primerL].getDato()
    def ultimoElemento(self):
        dato = None
        aux = self.__primerL
        while self.__arreglo[aux].getSiguiente() != -1:
            aux = self.__arreglo[aux].getSiguiente()
        dato = self.__arreglo[aux].getDato()
        return dato
    def siguiente(self, pos):
        valor = -1
        if (not self.vacia()):
            if (pos == 0):
                valor = self.__arreglo[self.__primerL].getSiguiente()
            else:
                i = 0
                aux = self.__primerL
                while self.__arreglo[aux].getSiguiente() != -1 and i < pos:
                    i += 1
                    aux = self.__arreglo[aux].getSiguiente()
                if (i == pos):
                    valor = self.__arreglo[aux].getSiguiente()
                    self.__cant += 1
        return valor
    def anterior(self, pos):
        valor = -1
        if (not self.vacia()):
            if (pos == 0):
                valor = None
            else:
                i = 1
                aux = self.__primerL
                while self.__arreglo[aux].getSiguiente() != -1 and i < pos:
                    i += 1
                    aux = self.__arreglo[aux].getSiguiente()
                if (i == pos):
                    valor = aux
        return valor

    def insertar(self, dato, pos):
        pos -= 1
        if (self.vacia()):
            if (pos == 0):
                nodo = Nodo(dato)
                self.__primerL = self.__primerD
                self.__primerD = self.__arreglo[
                    self.__primerD].getSiguiente()
                self.__arreglo[self.__primerL] = nodo
                self.__cant += 1
        elif (self.__primerD != -1):
            if (pos == 0):
                nodo = Nodo(dato)
                nodo.setSiguiente(self.__primerL)
                aux = self.__primerD
                self.__primerD = self.__arreglo[self.__primerD].getSiguiente()
                self.__arreglo[aux] = nodo
                self.__primerL = aux
                self.__cant += 1
            else:
                nodo = Nodo(dato)
                anterior = self.anterior(pos)
                if (anterior != -1):
                    siguiente = self.__arreglo[anterior].getSiguiente()
                    nodo.setSiguiente(siguiente)
                    aux = self.__primerD
                    self.__primerD = self.__arreglo[self.__primerD].getSiguiente()
                    self.__arreglo[anterior].setSiguiente(aux)
                    self.__arreglo[aux] = nodo
                    self.__cant += 1
                else:
                    raise IndexError
        else:
            raise IndexError('ERROR: lista llena')
    def suprimir(self, pos):
        valor = -1
        if (not self.vacia() and pos > 1 and pos < self.__cant + 1):
            pos -= 1
            if (pos == 0):
                aux = self.__primerL
                self.__primerL = self.__arreglo[self.__primerL].getSiguiente()
                self.__arreglo[aux].setSiguiente(self.__primerD)
                self.__primerD = aux
                self.__cant -= 1
            else:
                anterior = self.anterior(pos)
                if (anterior != -1):
                    aux = self.__arreglo[anterior].getSiguiente()
                    siguiente = self.__arreglo[aux].getSiguiente()
                    self.__arreglo[anterior].setSiguiente(siguiente)
                    self.__arreglo[aux].setSiguiente(
                        self.__primerD)
                    self.__primerD = aux
                    self.__cant -= 1
                else:
                    raise IndexError
        return valor
    def recuperar(self, pos):
        valor = -1
        if (not self.vacia() and pos > 1 and pos < self.__cant + 1):
            pos -= 1
            aux = self.__primerL
            i = 0
            while self.__arreglo[aux].getSiguiente() != -1 and i < pos:
                i += 1
                aux = self.__arreglo[aux].getSiguiente()
            if (i == pos):
                valor = self.__arreglo[aux].getDato()
            else:
                raise IndexError
        return valor

    def buscar(self, dato):
        pos = -1
        if (not self.vacia()):
            band = False
            aux = self.__primerL
            while not band and self.__arreglo[aux].getSiguiente() != -1:
                if (self.__arreglo[aux].getDato() == dato):
                    pos = aux
                    band = True
                aux = self.__arreglo[aux].getSiguiente()
        return pos

    def recorrer(self):
        lista = []
        aux = self.__primerL
        while self.__arreglo[aux].getSiguiente() != -1:
            lista.append(self.__arreglo[aux].getDato())
            aux = self.__arreglo[aux].getSiguiente()
        lista.append(self.__arreglo[aux].getDato())
        print('Memoria disponible: ', self.__primerD)
        return lista
