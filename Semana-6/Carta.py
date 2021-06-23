import random
from Enumerados import *

class Carta():

    # método constructor
    def __init__(varClase):
        # generar numero aleatorio entre 1 y 52
        varClase.indice = random.randrange(1, 53)

    def obtenerPinta(varClase):
        if varClase.indice <= 13:
            return PintaCarta.TREBOL
        elif varClase.indice <= 26:
            return PintaCarta.PICA
        elif varClase.indice <= 39:
            return PintaCarta.CORAZON
        else:
            return PintaCarta.DIAMANTE
        