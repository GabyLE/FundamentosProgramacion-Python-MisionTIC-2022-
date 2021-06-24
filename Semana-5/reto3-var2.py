def traducirPalabra(palabraM):
    morse2abc = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
    letras = palabraM.split()
    palabra = ""
    for letra in letras:
        palabra += morse2abc[letra]
    return palabra

def traductor_a_espanol(mensaje_a_traducir):
    palabras = mensaje_a_traducir.split("/")
    palabrasTraducidas = []
    for palabra in palabras:
        palabrasTraducidas.append(traducirPalabra(palabra))

    mensaje_traducido = " ".join(palabrasTraducidas)

    return mensaje_traducido