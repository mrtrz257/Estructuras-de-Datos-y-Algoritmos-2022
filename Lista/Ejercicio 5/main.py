from ListaEncad import ListaEncadenada

def inicializar():
    listaNum = [10, 5, 7, 5, 2, 10]
    lista = ListaEncadenada()
    i = 0
    for elemento in listaNum:
        lista.insertar(elemento, i)
        i += 1
    return lista

if __name__ == '__main__':
    lista = inicializar()
    print("Inicio")
    lista.recorrer()
    lista.verificar()
    print("Punto A")
    lista.recorrer()
    lista.verificar()
    lista.ordenar()
    print("Punto B")
    lista.recorrer()
