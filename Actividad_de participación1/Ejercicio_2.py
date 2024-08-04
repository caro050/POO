import random

cantidad_num = int(input("Ingrese la cantidad de números aleatorios a generar: "))

limite_inferior = int(input("Ingresa el límite inferior del rango: "))

limite_superior = int(input("Ingresa el límite superior del rango: "))

numeros_aleatorios = []
for _ in range(cantidad_num):
    numero = random.randint(limite_inferior, limite_superior)
    numeros_aleatorios.append(numero)

print("Lista de números aleatorios generada:", numeros_aleatorios)

















