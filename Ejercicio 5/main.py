from Pila import Pila
from Manejador import Manejador
from Controlador import Controlador

def Crear(dif):
    lista = []
    for i in range(3):
        pila = Pila(dif)
        if i == 0:
            for disco in range(dif, 0, -1):
                pila.insertar(disco)
        lista.append(pila)
    return lista

def Carga(manejador, pilas):
    for pila in pilas:
        manejador.cargarPila(pila)

if __name__ == '__main__':
    control = Controlador()
    dif = int(input("Ingrese cantidad de Discos (De 3 en adelante): "))
    manej = Manejador(dif)
    pilas = Crear(dif+1)
    Carga(manej, pilas)
    control.moveOptimo(dif)
    control.cargarManejador(manej)
    band = False
    final = False
    while not band:
        print(control.mostrar())
        print("Ingresar Fin para finalizar")
        orden1 = input("Quitar Disco: ")
        if orden1.lower() != "fin":
            if control.cargarOrdenInicial(orden1):
                orden2 = input("Colocar Disco: ")
                if control.cargarOrdenFinal(orden2):
                    control.mover()
            if control.Escaneo(dif):
                band = True
                final = True
        else:
            band = True
