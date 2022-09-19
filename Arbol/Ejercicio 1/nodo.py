class nodo:
    __item = 0
    __izq = None
    __der = None
    def __init__(self, item=0, izq = None, der=None):
        self.__item = item
        self.__izq = izq
        self.__der = der
    def getItem(self):
        return self.__item
    def cargarItem(self, x):
        self.__item = x
    def cargarIzquierdo(self, puntero):
        self.__izq = puntero
        return self.__izq
    def obtenerIzquierdo(self):
        return self.__izq
    def cargarDerecho(self, puntero):
        self.__der = puntero
        return self.__der
    def obtenerDerecho(self):
        return self.__der
