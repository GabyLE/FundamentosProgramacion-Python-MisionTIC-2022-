from Carta import Carta

class Baraja:
    
    def __init__(self):
        self.baraja = [True] * 52

    def verificaDisponibilidad(self, carta):
        return self.baraja[carta.indice - 1]

    def cambiaDisponibilidad(self, carta):
        self.baraja[carta.indice - 1] = False