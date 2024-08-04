
import math

def calcular_area(radio):
 
    area = math.pi * (radio ** 2)
    return area


radio = float(input("Ingrese por favor el radio del círculo: "))
area = calcular_area(radio)
print(f"El área del círculo  es {area:.2f}")
















