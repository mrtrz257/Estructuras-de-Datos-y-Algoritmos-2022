import random
from ColaSecuencial import ColaSec

def Aplicacion(FrecPacientes, TiempoAtencion):
    cola = ColaSec(10)
    number = random.uniform(0.4, 1)
    hospital = 0
    reloj = 0
    tiempoMaximo = 0
    cantidadPacientes = 0
    TMS = 240
    while reloj != TMS and cantidadPacientes<=9:
        frec = 0.5/FrecPacientes
        if number >= frec:
            cola.insertar(reloj)
        if hospital == 0:
            if not cola.vacia():
                paciente = cola.suprimir()
                cantidadPacientes += 1
                tiempoEsperaPaciente = reloj - paciente
                if tiempoMaximo < tiempoEsperaPaciente:
                    tiempoMaximo += tiempoEsperaPaciente
                hospital = TiempoAtencion
        reloj += 1
        if hospital>0:
            hospital -= 1
        number = random.uniform(0.4, 1)
    return tiempoMaximo/cantidadPacientes



if __name__ == '__main__':
    TiempoAtencion = 20
    FrecPacientes = 1
    t = Aplicacion(FrecPacientes, TiempoAtencion)
    print("Tiempo Promedio de Espera del Paciente: {:.1f} Minutos".format(t))
