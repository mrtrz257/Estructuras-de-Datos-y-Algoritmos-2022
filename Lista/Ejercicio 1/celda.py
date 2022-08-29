class Celda:
    __dato = None
    __siguiente = None
    def __init__(self):
        self.__dato = None
        self.__siguiente = Celda()
    def setDato(self, dato):
        self.__dato = dato
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__dato
        