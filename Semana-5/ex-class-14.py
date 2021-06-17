from Laberinto import Laberinto

laberinto = [[1,1,1,1,1,1,1,1,1,1], \
            [1,0,0,1,0,0,0,1,0,1], \
            [1,0,0,1,0,0,0,1,0,1], \
            [1,0,0,0,0,1,1,0,0,1], \
            [1,0,1,1,1,0,0,0,0,1], \
            [1,0,0,0,1,0,0,0,0,1], \
            [1,0,1,0,0,0,1,0,0,1], \
            [1,0,1,1,1,0,1,1,0,1], \
            [1,1,0,0,0,0,0,0,0,1], \
            [1,1,1,1,1,1,1,1,1,1]]

lab = Laberinto(laberinto, 1, 0, len(laberinto)-1, len(laberinto[0])-2)

print("El laberinto es:")
lab.mostrar()

if lab.resolver():
    print("El laberinto resuelto es:")
    lab.mostrar()
else:
    print("El laberinto no se puede resolver")