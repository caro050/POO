class CarroCompras:
    
    def __init__(self):
        self.items: list[ItemCompra] = []

    def agregar_item(self, libro: Libro, cantidad: int) -> ItemCompra:
        item = ItemCompra(libro, cantidad)
        self.items.append(item)
        return item

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self.items)

    def quitar_item(self, isbn: str) -> None:
        self.items = [item for item in self.items if item.libro.isbn != isbn]

