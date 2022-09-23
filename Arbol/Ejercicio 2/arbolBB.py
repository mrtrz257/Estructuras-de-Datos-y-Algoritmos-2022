from nodo import nodo

class arbolBB:
    __raiz = None
    __altura = None
    def __init__(self):
        self.__raiz = None
        self.__altura = 0
    def vacio(self):
        return self.__raiz == None
    def obtenerRaiz(self):
        return self.__raiz
    def mostrarRaiz(self):
        return self.__raiz.getItem()
    def insertar(self, x):
        if self.vacio():
            self.__raiz = nodo(x)
        else:
            aux = self.posicion(x)
            if aux != None:
                celda = nodo(x)
                clave = aux[0].getItem()
                if clave > x:
                    if aux[1]+1 > self.__altura:
                        self.__altura = aux[1]+1
                    aux[0].cargarIzquierdo(celda)
                elif clave < x:
                    if aux[1]+1 > self.__altura:
                        self.__altura = aux[1]+1
                    aux[0].cargarDerecho(celda)
            else:
                print("ERROR")
    def suprimir(self, x):
        pass
    def buscar(self, x):
        band = False
        elemento = self.posicion(x)[0]
        if elemento.getItem()==x:
            band = True
        return band
    def nivel(self, x):
        niv = 0
        elemento = self.posicion(x)
        if elemento[0].getItem()==x:
            niv = elemento[1]
        else:
            print("ERROR")
        return niv
    def hoja(self, x):
        band = False
        elemento = self.posicion(x)[0]
        if elemento.getItem()==x and elemento.obtenerIzquierdo() == None and elemento.obtenerDerecho()==None:
            band = True
        else:
            if elemento.getItem() != x:
                print("ERROR")
        return band
    def hijo(self, x, z):
        band = False
        celda = self.posicion(z)[0]
        if celda.getItem()==z:
            izq = celda.obtenerIzquierdo()
            if izq != None and izq.getItem()==x:
                band = True
            else:
                der = celda.obtenerDerecho()
                if der != None and der.getItem()==x:
                    band = True
        else:
            print("ERROR")
        return band
    def padre(self, z, x):
        band = False
        celda = self.posicion(z)[0]
        if celda.getItem() == z:
            izq = celda.obtenerIzquierdo()
            if izq != None and izq.getItem() == x:
                band = True
            else:
                der = celda.obtenerDerecho()
                if der != None and der.getItem() == x:
                    band = True
        else:
            print("ERROR")
        return band
    def camino(self, x, z):
        pass
    def altura(self):
        if self.vacio():
            print("Arbol Vacio")
        else:
            return self.__altura
    def InOrden(self):
        self.recursiva(self.__raiz.obtenerIzquierdo())
        print(self.__raiz.getItem())
        self.recursiva(self.__raiz.obtenerDerecho())
    def PrePorden(self):
        print(self.__raiz.getItem())
        self.recursiva(self.__raiz.obtenerIzquierdo())
        self.recursiva(self.__raiz.obtenerDerecho())
    def PostOrden(self):
        self.recursiva(self.__raiz.obtenerIzquierdo())
        self.recursiva(self.__raiz.obtenerDerecho())
        print(self.__raiz.getItem())
    def recursiva(self, nodo):
        if (nodo != None):
            self.recursiva(nodo.obtenerIzquierdo())
            print(nodo.getItem())
            self.recursiva(nodo.obtenerDerecho())
    def posicion(self, x, niv=0):
        if not self.vacio():
            posicion = [None, None]
            if self.__raiz.getItem()==x:
                posicion[0] = self.__raiz
                posicion[1] = niv
            else:
                aux = self.__raiz
                band = True
                while band:
                    clave = aux.getItem()
                    if clave == x:
                        band = False
                    elif clave > x:
                        if aux.obtenerIzquierdo()==None:
                            band = False
                        else:
                            niv += 1
                            aux = aux.obtenerIzquierdo()
                    else:
                        if aux.obtenerDerecho()==None:
                            band = False
                        else:
                            niv += 1
                            aux = aux.obtenerDerecho()
                posicion[0]=aux
                posicion[1]=niv
        return posicion
    def buscaHojas(self, nodo):
        if nodo != None:
            self.buscaHojas(nodo.obtenerIzquierdo())
            if nodo.obtenerIzquierdo() == None and nodo.obtenerDerecho() == None:
                print(nodo.getItem())
            self.buscaHojas(nodo.obtenerDerecho())
    def frontera(self):
        aux = self.__raiz
        self.buscaHojas(aux)