import random as rand
from hash import tablaHash

if __name__ == '__main__':
    cant = int(input('Ingrese la cantidad de claves: '))
    tabla = tablaHash(cant)
    for i in range(cant):
        clave = rand.randint(0, 2000)
        print(clave)
        tabla.insertar(clave)
    tabla.mostrar()
    clave = int(input('Clave a insertar: '))
    valor = tabla.insertar(clave)
    if(valor == 0):
        print('ERROR: la clave ya esta en la tabla')
    elif(valor == 1):
        print('DATO: la clave se inserto en la tabla')
    elif(valor == 2):
        print('DATO: la clave se inserto en otro lugar en la tabla')
    elif(valor == 3):
        print('ERROR: la tabla esta llena')
    tabla.mostrar()
    clave = int(input('Clave a buscar (-1 para salir): '))
    while clave != -1:
        valor = tabla.buscar(clave)
        if(valor == 0):
            print('DATO: la clave esta en la tabla')
        elif(valor == 1):
            print('ERROR: la clave no esta en la tabla')
        elif(valor == 2):
            print('DATO: la clave se inserto en otro lugar en la tabla')
        elif(valor == 3):
            print('ERROR: la tabla esta llena y no esta la clave')
        clave = int(input('Clave a buscar: '))
