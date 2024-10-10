class ItemCompra:
    def __init__ (self, libro: Libro, cantidad: int):
        self.libro = libro
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        return self.libro.precio * self.cantidad