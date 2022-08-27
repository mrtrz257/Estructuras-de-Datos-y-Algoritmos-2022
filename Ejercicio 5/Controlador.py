class Controlador:
    __inicio = None
    __final = None
    __manejador = None
    __mov = None
    __optimo = None
    def __init__(self):
        self.__inicio = None
        self.__final = None
        self.__manejador = None
        self.__mov = 0
        self.__optimo = None
    def moveOptimo(self, dif):
        self.__optimo = (2 ** dif) - 1
    def verificacionFinal(self, cont, dif):
        band = False
        i = 0
        long = len(cont)
        if (long == dif):
            band = True
        return band
    def Escaneo(self, dif):
        band = False
        cont = self.__manejador.Escaneo()
        if (self.verificacionFinal(cont, dif)):
            band = True
        return band
    def validarOrden(self, orden):
        band = False
        long = self.__manejador.getLen()
        try:
            orden = int(orden)
            if (orden > 0 and orden <= long):
                band = True
        except ValueError:
            band = False
        return band
    def cargarOrdenInicial(self, orden):
        band = True
        if (self.validarOrden(orden)):
            if (self.__manejador.getTope(int(orden)) != -1):
                self.__inicio = int(orden)
            else:
                band = False
        else:
            band = False
        return band
    def cargarOrdenFinal(self, orden):
        band = True
        if (self.validarOrden(orden) and int(orden) != self.__inicio):
            if (self.__manejador.getTope(int(orden)) == -1):
                self.__final = int(orden)
                self.__mov += 1
            elif (self.__manejador.getDatoTope(int(orden)) > self.__manejador.getDatoTope(self.__inicio)):
                self.__final = int(orden)
                self.__mov += 1
            else:
                band = False
        else:
            band = False
        return band
    def cargarManejador(self, manejador):
        self.__manejador = manejador
    def mover(self):
        self.__manejador.moverTope(self.__inicio, self.__final)
    def mostrar(self):
        text = '{}'.format(self.__manejador)
        return text
    def getMovimientos(self):
        return self.__mov
    def puntaje(self):
        band = False
        if (self.__mov == self.__optimo):
            band = True
        return band
