import winsound

class NotaMusical:

    def separarNota(notaCompleta):
            #separar la nota y la escala
            notaCompleta=notaCompleta.lower().strip()
            if notaCompleta.find("sol")>=0:
                if len(notaCompleta)==4:
                    nota=notaCompleta[:3]
                    escala=int(notaCompleta[3:])
                else:
                    nota=notaCompleta[:4]
                    escala=int(notaCompleta[4:])
            else:
                if len(notaCompleta)==3:
                    nota=notaCompleta[:2]
                    escala=int(notaCompleta[2:])
                else:
                    nota=notaCompleta[:3]
                    escala=int(notaCompleta[3:])
            return [nota, escala]

    def __init__(varClase, notaCompleta, figura):
        sn = NotaMusical.separarNota(notaCompleta)
        varClase.nota = sn[0]
        varClase.escala = int(sn[1])
        # escala 4
        notas = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
        valorD = []
        d = -9 # distancia en semitonos a la nota LA escala 4
        for n in notas:
            valorD.append(d)
            d += 1
        
        dNotas = dict(zip(notas, valorD))

        varClase.d = dNotas[varClase.nota]
        # define en qué escala
        if varClase.escala < 3:
            varClase.d -= (3 - varClase.escala) * 12
        else:
            varClase.d += (varClase.escala - 3) * 12

        t = 4000 # tiempo en milésimas de segundos

        figuras = ["semicorchea", "corchea", "negra", "blanca", "redonda"]
        tiempos = [16, 8, 4, 2, 1]

        dFiguras = dict(zip(figuras, tiempos))
        varClase.tiempo = int(t / dFiguras[figura.lower().strip()])

    def obtenerFrecuencia(varClase):
        r = 1.0594630943593
        return int(440 * r ** varClase.d)

    def reproducir(varClase):
        hz = varClase.obtenerFrecuencia()
        winsound.Beep(hz, varClase.tiempo)