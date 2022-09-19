from nodo import nodo

class arbolBB:
    __raiz = None
    def __init__(self):
        self.__raiz = None
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
            print(x)
            if self.__raiz.getItem()==x:
                print("Elemento ya Existe")
            else:
                if self.__raiz.getItem() > x:
                    return self.insertar(self.__raiz.obtenerIzquierdo())
                else:
                    return self.insertar(self.__raiz.obtenerDerecho())
    def suprimir(self, x):
        pass
    def buscar(self, x):
        if self.vacio():
            print("Elemento Inexistente")
        else:
            if self.__raiz.getItem()==x:
                return self.__raiz.getItem()
            else:
                if self.__raiz.getItem()<x:
                    return self.buscar(self.__raiz.obtenerIzquierdo())
                else:
                    return self.buscar(self.__raiz.obtenerDerecho())
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
