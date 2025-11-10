class LectorCodigo:
    def __init__(self, productos_registrados):
        self.productos_registrados = productos_registrados

    def escanear(self, codigo):
        return self.productos_registrados.get(codigo)

    def validar_codigo(self, codigo):
        return codigo in self.productos_registrados

    def __repr__(self):
        return f"{len(self.productos_registrados)} productos registrados"
