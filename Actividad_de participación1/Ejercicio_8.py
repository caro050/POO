
filas = int(input("Ingrese el número de filas que desee: "))
columnas = int(input("Ingrese el número de columnas que desee: "))

matriz = []
num = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(num)
        num += 1
    matriz.append(fila)

print("Esta fue la matriz que se genero:")
for fila in matriz:
    for numero in fila:
        print(numero, end=" ")
    print()














