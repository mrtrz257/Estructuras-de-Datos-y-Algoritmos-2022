class Cajero:
    __cliente = None
    __tiempoAtencion = None
    __tiempo = None
    def __init__(self, tiempoAtencion):
        self.__tiempoAtencion = tiempoAtencion
        self.__cliente = None
        self.__tiempo = 0
    def agregarCliente(self, cliente):
        if cliente != -1:
            self.__cliente = cliente
    def quitarCliente(self):
        cliente = None
        if self.__cliente != None:
            self.__cliente = None
        return cliente
    def AumentarTiempo(self):
        cliente = None
        if self.__cliente != None:
            if self.__tiempo < self.__tiempoAtencion:
                self.__tiempo += 1
            else:
                self.__tiempo = 0
                cliente = self.__cliente
                self.__cliente = None
        return cliente
    