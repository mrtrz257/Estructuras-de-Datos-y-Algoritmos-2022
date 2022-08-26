from nodo import Nodo

class ColaEnc:
    __cantidad = 0
    __pr = None
    __ul = None
    def __init__(self, pr=Nodo(), ul=Nodo(), cantidad=0):
        self.__pr = pr
        self.__ul = ul
        self.__cantidad = cantidad
    def vacia(self):
        return self.__cantidad == 0
    def insertar(self, x):
        ps1 = self.__pr
        ps1.setDato(x)
        ps1.setSiguiente(None)
        if self.__ul == None:
            self.__pr = ps1
        else:
            self.__ul.setSiguiente(ps1)
            self.__ul = ps1
            self.__cantidad += 1
            return self.__ul.geDato()
    def suprimir(self):
        if self.vacia():
            print("Pila Vacia")    
            return 0
        else:
            aux = self.__pr
            x = self.__pr.geDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cantidad -= 1
            #if self.__pr==None:
            del aux
            return x
        