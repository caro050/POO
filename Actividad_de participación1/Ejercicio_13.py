num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

sum = num1 + num2
rest = num1 - num2
multi = num1 * num2

if num2 != 0:
    division = num1 // num2  
else:
    division = "No se puede dividir por cero"

print(f"La suma de {num1} y {num2} es: {sum} ")
print(f"La resta de {num1} y {num2} es: {rest} ")
print(f"La multiplicación de {num1} y {num2} es: {multi} ")
print(f"La división de {num1} y {num2} es: {division} ")














