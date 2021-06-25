from Carta import Carta

class Baraja:

    def __init__(varClase):
        # Baraja del juego, todas las cartas están disponibles
        varClase.baraja = [True] * 52

    def verificaDisponibilidad(varClase, carta):
        # Retorna True si la carta esta disponible de lo contrario retorna False si ya salió
        return varClase.baraja[carta.indice - 1]

    def cambiaDisponibilidad(varClase, carta):
        varClase.baraja[carta.indice - 1] = False