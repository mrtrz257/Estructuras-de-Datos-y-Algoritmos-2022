from nodo import nodo

class arbolBB:
    __raiz = None
    def __init__(self):
        self.__raiz = None
    def vacio(self):
        return self.__raiz == None
    def insertarRaiz(self, x):
        aux = nodo(x)
        self.__raiz = aux
    def obtenerRaiz(self):
        return self.__raiz
    def mostrarRaiz(self):
        return self.__raiz.getItem()
    def insertar(self, x):
        if self.vacio():
            self.__raiz = nodo(x)
        else:
            if self.__raiz.getItem()==x:
                print("Elemento ya Existe")
            else:
                if self.__raiz.getItem() < x:
                    self.__raiz.cargarIzquierdo(x)
                else:
                    self.__raiz.cargarDerecho(x)
    def suprimir(self, x):
        pass
    def buscar(self, x):
        if self.vacio():
            print("Elemento Inexistente")
        else:
            if self.__raiz.getItem()==x:
                return self.__raiz.getItem()
            else:
                print("{} {}".format(self.__raiz.getItem(), x))
                if self.__raiz.getItem()<x:
                    aux = int(self.__raiz.obtenerIzquierdo())
                    return self.buscar(aux)
                else:
                    aux = int(self.__raiz.obtenerDerecho)
                    return self.buscar(aux)
    def nivel(self, x):
        pass
    def hoja(self, x):
        pass
    def hijo(self, x, z):
        pass
    def padre(self, x, z):
        pass
    def camino(self, x, z):
        pass
    def altura(self):
        pass
    def InOrden(self):
        if not self.vacio():
            self.InOrden()


    def PrePorden(self):
        pass
    def PostOrden(self):
        pass
