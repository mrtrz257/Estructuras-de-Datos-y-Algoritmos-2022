import numpy as np

class DirecAbierto:
    __tabla = None
    def __init__(self):
        self.__tabla = None
    def crear(self, numClaves):
        tamTabla = int(numClaves/0.7)               #1428 no es primo
        self.__tabla = np.empty(tamTabla, dtype=int)
    def insertar(self, clave, rand, numClaves):
        tamTabla = int(numClaves/0.7)
        mod = clave % tamTabla
        if self.__tabla[mod] != clave:
            self.__tabla[mod] = clave
        else:
            self.__tabla[mod+rand] = clave
