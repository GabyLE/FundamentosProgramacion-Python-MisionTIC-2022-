from Carta import Carta
from Enumerados import *
from Baraja import Baraja

class Jugador():

    TOTAL_CARTAS = 10

    def __init__(varClase):
        varClase.cartas = []

    # def repartir(varClase):
    #     varClase.cartas = []
    #     for i in range(Jugador.TOTAL_CARTAS):
    #         c = Carta()
    #         varClase.cartas.append(c)

    def repartir(varClase, b):
        
        varClase.cartas = []
        cond = 0
        while cond != -1:
            c = Carta()
            if b.verificaDisponibilidad(c) and len(varClase.cartas) < 10:
                varClase.cartas.append(c)
                b.cambiaDisponibilidad(c)

            if len(varClase.cartas) == Jugador.TOTAL_CARTAS:
                cond = -1
                

    def mostrar(varClase, frm):
        x = 10
        for c in varClase.cartas:
            c.mostrar(frm, x, 10 )
            x += 40

    def verificar(varClase):
        contadores = [0] * 13
        
        for c in varClase.cartas:
            p = c.obtenerIndiceNumero() - 1
            contadores[p] += 1

        mensaje = "Las figuras encontradas fueron: "
        for i in range(13):
            if contadores[i] >= 2:
                g = GrupoCarta(contadores[i])
                nc = NombreCarta(i + 1)

                # name -> atributo de los enumerados para el nombre
                mensaje += "\n" + g.name + " de " + nc.name

        return mensaje