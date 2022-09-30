from arbolBB import arbolBB

if __name__ == '__main__':
    arbol = arbolBB()
    arbol.insertar(9)
    arbol.insertar(4)
    arbol.insertar(13)
    arbol.insertar(2)
    arbol.insertar(15)
    arbol.insertar(5)
    arbol.insertar(10)
    arbol.insertar(3)
    print("Altura del arbol: ", arbol.altura())
    print("Cantidad de Nodos en el arbol: ", arbol.contador())
    
