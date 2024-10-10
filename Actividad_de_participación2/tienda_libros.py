class TiendaLibros:
    
    # Defina metodo inicializador __init__

    def __init__(self, catalogo: dict[str, Libro], carrito:CarroCompras):
        self.catalogo = catalogo
        self.carrito = carrito
    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int):

        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        else:
            self.catalogo[isbn] = Libro(isbn, titulo, precio, existencias)
            return self.catalogo
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        elif libro.existencias < cantidad:
            raise ExistenciasinsuficientesError(libro.titulo, libro.isbn, cantidad)
        else:
            self.carrito.agregar_libro(libro, cantidad)
            self.catalogo[libro.isbn].existencias -= cantidad
            return self.carrito
    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn: str):
        self.carrito.quitar_item(isbn)