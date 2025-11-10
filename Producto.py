class Producto:
    def __init__(self, codigo, nombre, precio_u, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_u = precio_u
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def __repr__(self):
        return f"{self.codigo} - {self.nombre} - ${self.precio_u:.2f} - Stock: {self.stock}"


