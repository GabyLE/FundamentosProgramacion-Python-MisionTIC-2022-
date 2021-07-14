from Carta import Carta
from Baraja import Baraja

class Jugador:

    TOTAL_CARTAS = 10

    def __init__(self):
        self.cartas = []

    def repartir(self, baraja):
        self.cartas = []
        cond = 0
        while cond < Jugador.TOTAL_CARTAS:
            c  = Carta()
            if baraja.verificaDisponibilidad(c):
                self.cartas.append(c)
                baraja.cambiaDisponibilidad(c)
                cond += 1

    def mostrar(self, frame):
        col = 0
        for c in self.cartas:
            c.mostrarCarta(0, col, frame)
            col += 1

