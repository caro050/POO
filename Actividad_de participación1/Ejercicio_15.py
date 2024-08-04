def palindromo(cadena):
  
    cadena_normal = ''.join(cadena.lower().split())
 
    return cadena_normal == cadena_normal[::-1]

text = input("Ingrese una cadena de texto: ")

if palindromo(text):
    print("La cadena es un palíndromo ")
else:
    print("La cadena no es un palíndromo ")














