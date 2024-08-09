class Carta:
   
    Corazones = "Corazones"
    Diamantes = "Diamantes"
    Treboles = "Tréboles"
    Picas= "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return f"{self.valor} de {self.pinta}"

cart = Carta(10, Carta.Diamantes)
print(cart)  
