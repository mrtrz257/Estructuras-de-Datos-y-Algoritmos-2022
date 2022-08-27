from Pila import Pila

def Ejercicio4():
    pila = Pila(8)
    band = True
    while band:
        pil = int(input("Ingrese Pila (0 para finalizar): "))
        if pil != 0:
            num = int(input("Ingrese Numero: "))
            if pil == 1:
                if pila.insertar1(num) == 0:
                    print("Pila llena")
            elif pil == 2:
                if pila.insertar2(num) == 0:
                    print("Pila llena")
            else:
                print("Pila no existe")
        else:
            band = False
    print("Pila 1:")
    pila.mostrar1()
    print("Pila 2:")
    pila.mostrar2()

if __name__ == '__main__':
    Ejercicio4()
