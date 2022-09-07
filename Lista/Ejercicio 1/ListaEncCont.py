from Nodo import Nodo

class ListaEncCont:
    __primer = None
    __cant = None
    def __init__(self):
        self.__primer = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def primerElemento(self):
        valor = -1
        if(not self.vacia()):
            valor = self.__primer.getDato()
        return valor
    def ultimoElemento(self):
        valor = -1
        if(not self.vacia()):
            aux = self.__primer
            while aux.getSiguiente() != None:

                aux = aux.getSiguiente()
            valor = aux.getDato()
        return valor
    def siguiente(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__primer.getSiguiente()
            else:
                i = 0
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if(i == pos):
                    valor = aux.getSiguiente()
        return valor
    def anterior(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = None
            else:
                i = 1
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                if(i == pos):
                    valor = aux
        return valor
    def insertar(self, dato):
        if(self.vacia()):
            self.__primer = Nodo(dato)
            self.__cant += 1
        else:
            nodo = Nodo(dato)
            if(self.primerElemento() > dato):
                nodo.setSiguiente(self.__primer)
                self.__primer = nodo
                self.__cant += 1
            else:
                ultimo = self.ultimoElemento()
                if(ultimo < dato):
                    aux = self.__primer
                    while aux.getSiguiente() != None:
                        aux = aux.getSiguiente()
                    aux.setSiguiente(nodo)
                    self.__cant += 1
                if(dato > self.primerElemento() and dato < ultimo):
                    aux = self.__primer
                    band = False
                    i = 0
                    while aux.getSiguiente() != None and not band:
                        if(aux.getDato() > dato):
                            band = True
                        i += 1
                        aux = aux.getSiguiente()
                    nodo.setSiguiente(aux)
                    anterior = self.anterior(i)
                    anterior.setSiguiente(nodo)
                    self.__cant += 1

    def suprimir(self, dato):
        valor = -1
        if(not self.vacia()):
            pos = self.buscar(dato)
            if(pos == 0):
                self.__primer = self.__primer.getSiguiente()
                self.__cant -= 1
            else:
                anterior = self.anterior(pos)
                if(anterior != -1):
                    aux = anterior.getSiguiente()
                    siguiente = aux.getSiguiente()
                    anterior.setSiguiente(siguiente)
                    self.__cant -= 1
                else:
                    raise IndexError
        return valor
    def recuperar(self, pos):
        valor = -1
        if(not self.vacia()):
            if(pos == 0):
                valor = self.__primer.getDato()
            else:
                i = 0
                aux = self.__primer
                while aux.getSiguiente() != None and i < pos:
                    i += 1
                    aux = aux.getSiguiente()
                valor = aux.getDato()
        return valor
    def buscar(self, dato):
        pos = -1
        if(not self.vacia()):
            i = 0
            aux = self.__primer
            while aux != None and pos == -1:
                if(aux.getDato() == dato):
                    pos = i
                i += 1
                aux = aux.getSiguiente()
        return pos
    def recorrer(self):
        lista = []
        if(not self.vacia()):
            aux = self.__primer
            while aux != None:
                lista.append(aux.getDato())
                aux = aux.getSiguiente()
        print(lista)
