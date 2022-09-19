from arbolBB import arbolBB

if __name__ == '__main__':
    arbol = arbolBB()
    arbol.insertarRaiz(4)
    arbol.insertar(6)
    arbol.insertar(1)
    print(arbol.buscar(1))
    print(arbol.mostrarRaiz())
