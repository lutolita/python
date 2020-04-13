def vueltas(radio, distancia):
    # distancia por vuelta = 2.pi.R
    distVuelta = 2 * 3.14 * radio
    cantVueltas = distancia / distVuelta
    return cantVueltas


# Diametro de la llanta = 50 cm entonces radio = 25 cm en un kilometro o 100000 cm
print("La cantidad de vueltas que da una rueda de 50 cm de diametro es ", vueltas(25, 100000))