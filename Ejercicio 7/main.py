import random
from ColaSecuencial import ColaSec

def Aplicacion(FrecClientes, TiempoCajero):
    cola = ColaSec(20)
    number = random.uniform(0, 0.6)
    cajero = 0
    reloj = 0
    tiempoMaximo = 0
    TMS = 60
    while reloj != TMS:
        frec = 1/FrecClientes
        if number >= frec:
            cola.insertar(reloj)
        if cajero == 0:
            if not cola.vacia():
                cliente = cola.suprimir()
                tiempoEsperaCliente = reloj - cliente
                if tiempoMaximo < tiempoEsperaCliente:
                    tiempoMaximo += tiempoEsperaCliente
                cajero = TiempoCajero
        reloj += 1
        if cajero>0:
            cajero -= 1
        number = random.uniform(0, 0.6)
    return tiempoMaximo


if __name__ == '__main__':
    TACaj = int(input("Ingrese tiempo de atencion de cajero: "))
    FrecClientes = int(input("Ingrese frecuencia de llegada de clientes: "))
    t = Aplicacion(FrecClientes, TACaj)
    print("Tiempo Maximo de Espera de Cliente: {} Minutos".format(t))
