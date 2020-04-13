	seguir = 1
	estaturas = []
	continuar = 1


	def promediar(lista):
	    sum = 0
	    for item in lista:
	        sum += int(item)
	    return sum / len(lista)


	while int(seguir) == 1:
	    estatura = input("Ingrese estatura\n")
	    estaturas.append(estatura)
	    seguir = input("Si desea ingresar otra estatura ingrese 1, sino ingrese 0\n")
	print("el promedio de estatura es", promediar(estaturas))