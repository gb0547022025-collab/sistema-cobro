from barcode import EAN13
from barcode.writer import ImageWriter
import os

from Producto import Producto

class ProductoRepository:
    def __init__(self):
        self.productos = [
    Producto("001011203001", "Teclado Mecánico RGB", 45.0, 10),
    Producto("001022345560", "Switches Cherry MX Red", 0.5, 100),
    Producto("001031204563", "Keycaps Anime", 25.0, 20),
    Producto("001040214039", "Cable USB-C trenzado", 8.0, 50),
    Producto("001052045796", "Base acrílica transparente", 12.0, 15),
    Producto("761303539620", "Base acrílica azul", 10.0, 12)  
]


    def actualizar_stock(self, codigo, cantidad_vendida):
        for producto in self.productos:
            if producto.codigo == codigo:
                if producto.stock >= cantidad_vendida:
                    producto.stock -= cantidad_vendida
                    return True
                else:
                    print("Stock insuficiente.")
                    return False
        print("Producto no encontrado.")
        return False

    def get_dict(self):
        return {p.codigo: p for p in self.productos}

    def generar_codigos_barras(self):
        carpeta = "codigos"
        os.makedirs(carpeta, exist_ok=True)
        for producto in self.productos:
            archivo = os.path.join(carpeta, f"{producto.nombre.replace(' ', '_')}_{producto.codigo}")
            barcode = EAN13(producto.codigo, writer=ImageWriter())
            barcode.save(archivo)
        print(f"Códigos de barras generados en la carpeta '{carpeta}'.")


