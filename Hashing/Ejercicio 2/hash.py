import numpy as np
import random

class tablaHash:
    __arreglo = None
    def __init__(self, claves):
        cant = self.cantNoPrimo(claves//0.7)
        self.__arreglo = np.empty(cant, dtype=int)
        self.incializar()
    def insertar(self, clave, rand):
        pos = clave % len(self.__arreglo)
        if(self.__arreglo[pos] == -1): #se inserto la clave en la posicion
            self.__arreglo[pos] = clave
            valor = 1
        else:
            if(self.__arreglo[pos] != clave):
                i = pos-1
                while self.__arreglo[i] != -1 and self.__arreglo[i] != clave and i != pos:
                    i = (i-rand) % len(self.__arreglo)
                if(self.__arreglo[i] == -1): #se inserto la clave en otra posicion
                    self.__arreglo[i] = clave
                    valor = 2
                elif(self.__arreglo[i] == clave):
                    valor = 0
                else: #la tabla esta llena
                    valor = 3
            else:
                valor = 0
        return valor
    def buscar(self, clave, rand):
        pos = clave % len(self.__arreglo)
        long = 0
        if(self.__arreglo[pos] == -1): #posicion vacia
            valor = 1
        else:
            if(self.__arreglo[pos] != clave): #en la posicion hay una clave distinta
                i = pos-1
                long += 1
                while self.__arreglo[i] != clave and i != pos:
                    long += 1
                    i = (i-rand) % len(self.__arreglo)
                if(self.__arreglo[i] == clave): #se encuentra la clave en otra posicion
                    valor = 2
                else: #no se encuentra la clave en la tabla
                    valor = 3
            else:
                valor = 0
        print('La longitud de la Secuencia de Prueba Lineal:', long)
        return valor
    def incializar(self): #inicializa el arreglo
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = -1
    def cantPrimo(self, cant): #devuelve una cantidad primo
        lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        primo = -1
        i = 0
        band = False
        if(cant < lista[len(lista)-1]):
            while not band and i < len(lista):
                if(lista[i] > cant):
                    primo = lista[i]
                    band = True
                i += 1
        else:
            while not band and i <= 39:
                resultado = (i**2) + i + 41
                if(resultado > cant):
                    primo = resultado
                    band = True
                i += 1
        return primo
    def cantNoPrimo(self, cant): #devuelve una cantidad no primo
        dim = int(cant)
        if(self.primo(cant)):
            dim += 1
        return dim
    def primo(self, cant): #verifica si la cantidad es primo o no
        band = True
        div = 2
        while div < cant and band:
            if(cant % div == 0):
                band = False
            div += 1
        return band
    def GeneraPseudoRandom(self):   #Genera Un numero Pseudo Aleatorio para la secuencia de prueba
        pseudoRand = int(random.uniform(1, 6))
        return pseudoRand
    def mostrar(self):
        print('Tabla Hash:', self.__arreglo)
