
def F_a_C(fahrenheit):
   
    
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = F_a_C(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
















