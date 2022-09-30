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
    #print("Buscar 7 en el arbol", arbol.buscar(7))
    #print("Buscar 10 en el arbol", arbol.buscar(10))
    print("Altura del arbol: ", arbol.altura())
    print("Cantidad de Nodos en el arbol: ", arbol.contador())
    print("------------------")
    '''print("Nivel de 9:", arbol.nivel(9))
    print("Nivel de 15:", arbol.nivel(15))
    print("4 es hoja?", arbol.hoja(4))
    print("5 es hoja?", arbol.hoja(5))
    print("4 padre de 2:", arbol.padre(4,2))
    print("10 padre de 5:", arbol.padre(10,5))
    print("2 hijo de 4:", arbol.hijo(2,4))
    print("5 hijo de 10:", arbol.hijo(5,10))
    print("Frontera del arbol:")'''
    #arbol.frontera()


