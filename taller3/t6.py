    valores = []


    def fibonacci(actual, cantidad):
        index = actual
        while (index < cantidad):
            if index == 0:
                valores.append(0)
            elif index == 1:
                valores.append(1)
            else:
                valores.append(valores[actual - 1] + valores[index - 2])
            index += 1


    def imprimir(lista):
        for i in lista:
            print(i)


    cantidad = input("Cuantos valores desea generar?\n")
    fibonacci(0, int(cantidad))
    imprimir(valores)