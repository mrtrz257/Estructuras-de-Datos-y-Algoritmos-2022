from Pila import Pila

def Factorial(numero):
    pila = Pila(8)
    for i in range(numero):
        pila.insertar(numero-i)
    return pila

if __name__ == '__main__':
    num = int(input("Ingrese numero para calcular Factorial: "))
    fact = Factorial(num)
    print(fact.mostrar())
