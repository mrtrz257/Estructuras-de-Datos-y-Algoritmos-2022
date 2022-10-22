import numpy as np
import random

class DirecAbierto:
    __tabla = None
    def __init__(self):
        self.__tabla = None
    def crear(self, numClaves):
        tamTabla = self.CalcularTamanioTabla(numClaves)           #1428 no es primo
        self.__tabla = np.empty(tamTabla, dtype=int)
        for i in range(tamTabla):
            self.__tabla[i]=-1
    def insertar(self, clave, rand, tamTabla):
        mod = clave % tamTabla
        if self.__tabla[mod] == clave:
            return 0
        elif self.__tabla[mod] == -1:
            self.__tabla[mod] = clave
            return 1
        else:
            while self.__tabla[mod] != -1:
                mod += rand
            if self.__tabla[mod] == -1:
                self.__tabla[mod] = clave
            return 2
    def buscar(self, clave, tamTabla): #ARREGLAR
        mod = clave % tamTabla
        if self.__tabla[mod] == clave:
            return 1
        else:
            return -1
    def CalcularTamanioTabla(self, numClaves):
        tamTabla = int(numClaves/0.7)
        ###Permitir numeros primos###
        return tamTabla
    def GenerarPseudoRandom(self):
        pseudoRand = int(random.uniform(1, 6))
        return pseudoRand
