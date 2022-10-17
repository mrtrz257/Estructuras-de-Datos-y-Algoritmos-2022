import random

from Hashing import DirecAbierto

if __name__ == '__main__':
    tabla = DirecAbierto()
    pseudoRand = int(random.uniform(1, 6))
    numeroClaves = 1000
    tabla.crear(numeroClaves)
    for i in range(numeroClaves):
        clave = int(random.uniform(0, 2000))
        tabla.insertar(clave, pseudoRand, numeroClaves)
