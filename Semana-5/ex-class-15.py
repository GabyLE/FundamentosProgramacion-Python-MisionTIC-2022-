estudiantes = ["ACOSTA DANIEL ", \
	"AGUDELO QUICENO JUANITA ", \
	"ALARCÓN CELIS ALEJANDRO ", \
	"ALDANA MONTEALEGRE JHON JAIRO ", \
	"ALOMIA MANUEL ", \
	"ALZATE POSADA ANA MARÍA ", \
	"ANDREA ROCHA", \
	"AYALA S MARIA CRISTINA", \
	"BARRERA VALDÉS NATALIA ", \
	"BARRERO JOHN", \
	"BEDOYA T JUAN DIEGO ", \
	"BEJARANO PACHÓN JUAN SEBASTIÁN ", \
	"BELTRAN RICO ANDRÉS FELIPE ", \
	"BOHÓRQUEZ CABRERA JUAN JOSÉ ", \
	"BOHÓRQUEZ ESPINOSA ANDREA MILENA ", \
	"BOHORQUEZ IBAÑEZ JIMMY ALEJANDRO ", \
	"BUITRAGO ROBERT ", \
	"CALDERÓN PAULA", \
	"CALLE ESPINOSA CRISTINA ", \
	"CAMPOS CASTELLANOS ANA RAQUEL " ]
	
notas = [[2.4, 3.9, 3.9, 4.2], \
	[3.6, 2.4, 2.9, 4.7], \
	[2.3, 3.3, 2.9, 4.3], \
	[3.7, 3.7, 4.7, 2.9], \
	[4.4, 2.0, 4.6, 3.4], \
	[3.6, 3.3, 2.5, 2.8], \
	[2.6, 4.8, 2.9, 4.3], \
	[4.1, 2.7, 2.1, 2.6], \
	[3.6, 4.0, 4.5, 4.9], \
	[2.4, 2.9, 3.5, 4.8], \
	[2.6, 3.4, 4.2, 3.2], \
	[2.0, 3.3, 4.5, 3.8], \
	[4.5, 2.4, 4.3, 3.0], \
	[3.7, 4.2, 4.6, 4.1], \
	[2.1, 3.6, 2.0, 3.6], \
	[4.4, 2.9, 2.5, 4.3], \
	[3.1, 4.6, 2.6, 4.6], \
	[2.9, 4.9, 4.7, 4.0], \
	[2.5, 4.7, 3.4, 2.6], \
	[3.7, 2.8, 2.2, 4.8]]

porcentajes = [20, 30, 25, 25]

promedios = []

for fila in range(0, len(notas)):
	promedio = 0
	for columna in range(0, len(notas[0])):
		promedio += notas[fila][columna] * porcentajes[columna] / 100
	
	print(estudiantes[fila], ": {:.1f}".format(promedio))
	promedios.append(promedio)

# buscar la POSICION del mayor es más eficiente que buscar el VALOR del mayor dentro del vector
pos = 0
for i in range(1, len(promedios)):
	if promedios[i] > promedios[pos]:
		pos = i

print("El mayor promedio lo obtuvo", estudiantes[pos], "con un promedio de {:.1f}".format(promedios[pos]))

	
