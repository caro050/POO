from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int, existencias_disponibles: int):
        super().__init__(f"El libro con el título {titulo} y ISBN {isbn} no tiene suficiente existencia. "
                         f"Cantidad solicitada: {cantidad_a_comprar}, existencias disponibles: {existencias_disponibles}")
        self.titulo = titulo
        self.isbn = isbn
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias_disponibles = existencias_disponibles

    def __str__(self):
        return (f"El libro con título {self.titulo} y ISBN {self.isbn} no tiene suficientes existencias. "
                f"Cantidad a comprar: {self.cantidad_a_comprar}, existencias disponibles: {self.existencias_disponibles}")
