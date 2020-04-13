calificaciones = {'calculo': 3, 'fisica': 5, 'quimica': 2, 'ingles': 4, 'filosofia': 3.5, 'sociales': 3.6, 'literatura': 4.1, 'musica': 3.7, 'teconologia': 2.7, 'artistica': 4.9}

nombres = tuple(calificaciones.keys())
notas = tuple(calificaciones.values())
notaAlta = nombres[notas.index(max(notas))]
print('La materia con la nota más alta es ', notaAlta)