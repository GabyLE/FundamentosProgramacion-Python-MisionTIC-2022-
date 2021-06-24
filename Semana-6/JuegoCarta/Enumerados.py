from enum import Enum

# enumerado para la lista de pintas
class PintaCarta(Enum):
    TREBOL = 1
    PICA = 2
    CORAZON = 3
    DIAMANTE = 4

# enumerado para los grupos 
class GrupoCarta(Enum):
    VACIO = 0
    NON = 1
    PAR = 2
    TERNA = 3
    CUARTA = 4
    QUINTA = 5
    SEXTA = 6
    SEPTIMA = 7
    OCTAVA = 8
    NOVENA = 9
    DECIMA = 10    

# enumerado para los nombres de las cartas
class NombreCarta(Enum):
    AS = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    OCHO = 8
    NUEVE = 9
    DIEZ = 10
    JACK = 11
    QUEEN = 12
    KING = 13