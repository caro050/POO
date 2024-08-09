import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx**2 + dy**2) ** 0.5
    
punto1 = Punto(8, 4)
punto1.mostrar()  

punto2 = Punto(6, 8)
distancia = punto1.calcular_distancia(punto2)
print(f"La distancia es de: {distancia}")  

punto1.mover(10, 10)
punto1.mostrar()  


class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        largo = abs(self.punto2.x - self.punto1.x)
        ancho = abs(self.punto2.y - self.punto1.y)
        return 2 * (largo + ancho)

    def calcular_area(self):
        largo = abs(self.punto2.x - self.punto1.x)
        ancho = abs(self.punto2.y - self.punto1.y)
        return largo * ancho

    def es_cuadrado(self):
        largo = abs(self.punto2.x - self.punto1.x)
        ancho = abs(self.punto2.y - self.punto1.y)
       

p1 = Punto(4, 6)
p2 = Punto(4, 4)
rectangulo = Rectangulo(p1, p2)

print(f"El Perímetro del rectángulo es: {rectangulo.calcular_perimetro()}")  
print(f"El Área del rectángulo es : {rectangulo.calcular_area()}")            


if rectangulo.es_cuadrado():
    print("Es cuadrado.")
else:
    print("No es cuadrado.")
             

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        return self.centro.calcular_distancia(punto) <= self.radio
    

centro = Punto(0, 0)
circulo = Circulo(centro, 6)

print(f"El Área del círculo es de: {circulo.calcular_area()}")                  
print(f"El Perímetro del círculo es de : {circulo.calcular_perimetro()}")        
punto = Punto(3, 4)
print(f"¿El punto pertenece al círculo? {circulo.punto_pertenece(punto)}")  