from datetime import datetime

class Venta:
    def __init__(self, lector, ticket_actual):
        self.lector = lector
        self.ticket_actual = ticket_actual
        self.fecha = datetime.now()

    def escanear_producto(self, codigo):
        if self.lector.validar_codigo(codigo):
            return self.lector.escanear(codigo)
        else:
            print("Código inválido.")
            return None

    def agregar_al_ticket(self, codigo, cantidad):
        producto = self.escanear_producto(codigo)
        if producto and producto.stock >= cantidad:
            self.ticket_actual.agregar_producto(producto, cantidad)
        else:
            print("Stock insuficiente o producto no encontrado.")

    def finalizar_compra(self, repo_ventas):
        print(self.ticket_actual.mostrar_ticket())
        repo_ventas.guardar_venta(self)

    def finalizar_compra(self, repo_ventas):
        self.ticket_actual.mostrar_ticket() 
        archivo = self.ticket_actual.generar_ticket_pdf() 
        print(f"Factura guardada en: {archivo}")
        print(f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}")
        repo_ventas.guardar_venta(self)
