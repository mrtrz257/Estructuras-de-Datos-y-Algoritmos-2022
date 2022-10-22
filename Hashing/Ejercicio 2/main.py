import random
from Hashing import DirecAbierto

if __name__ == '__main__':
    tabla = DirecAbierto()
    pseudoRand = tabla.GenerarPseudoRandom()
    numeroClaves = 8.4
    tabla.crear(numeroClaves)
    tamanio = tabla.CalcularTamanioTabla(numeroClaves)
    print("-_________________________________-")
    '''for i in range(numeroClaves):
        clave = int(random.uniform(0, 1000))
        tabla.insertar(clave, pseudoRand, tamanio)
    clv = int(input("Ingresar para buscar: "))
    busq = tabla.buscar(clv, tamanio)
    if busq == -1:
        print("No se encontro la clave")
    else:
        print("Se encontro la clave {}".format(clv))'''
