class Manejador:
    __cajero = None
    __cola = None
    __maximo = None
    def __init__(self, cajero=None, cola=None):
        self.__cajero = cajero
        self.__cola = cola
        self.__maximo = 0
    def InsertarCliente(self, cliente):
        self.__cola.insertar(cliente)
    def getMaximo(self):
        return self.__maximo
    