class Punto:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mostrar(self):
        print(f"({self.a}, {self.b})")

    def mover(self, newx, newy):
        self.x = newx
        self.y = newy

    def calcular_distancia(self, otro_punto):
        da = self.a - otro_punto.a
        db = self.b - otro_punto.b
        return (da**2 + db**2) ** 0.5

punto1 = Punto(8, 4)
punto1.mostrar()  

punto2 = Punto(6, 8)
distancia = punto1.calcular_distancia(punto2)
print(f"La distancia es de: {distancia}")  

punto1.mover(10, 10)
punto1.mostrar() 













