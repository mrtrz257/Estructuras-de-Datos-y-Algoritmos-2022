from Pila import Pila

def ConversionBinario(numero):
    pila = Pila(8)
    band = True
    while band:
        resto = numero % 2
        numero = numero // 2
        if numero < 2:
            pila.insertar(resto)
            pila.insertar(numero)
            band = False
        else:
            pila.insertar(resto)
    return pila

if __name__ == '__main__':
    num = int(input("Ingrese Numero para Convertir a Binario: "))
    bin = ConversionBinario(num)
    bin.mostrar()
