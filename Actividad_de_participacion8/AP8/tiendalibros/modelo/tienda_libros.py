class TiendaLibros:
   class Tienda:
    def __init__(self, catalogo: dict[str, Libro], carrito: CarroCompras):
        self.catalogo = catalogo
        self.carrito = carrito

    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        self.catalogo[isbn] = Libro(isbn, titulo, precio, existencias)

    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int):
        if libro.existencias < cantidad:
            raise ExistenciasinsuficientesError(libro.titulo, libro.isbn, cantidad)
        self.carrito.agregar_libro(libro, cantidad)
        self.catalogo[libro.isbn].existencias -= cantidad

    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)
