from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        super().__init__(f"El libro con titulo {titulo} y isbn {isbn} está agotado")
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return self.args[0]
