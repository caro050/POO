print("Bienvenid@, si desea calcular el factorial de algun numero solo digite el numero que desee")

def factorial(n):
   
    if n < 0:
        return 
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num= int(input("Ingrese el numero que desee para obtener su factorial "))
result = factorial(num)
print(f"El factorial de" ,num, "es" ,result,)














