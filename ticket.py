from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import os

class Ticket:
    def __init__(self, numero_ticket, cliente):
        self.numero_ticket = numero_ticket
        self.cliente = cliente
        self.productos = []
        self.total = 0.0
        self.fecha = datetime.now()

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        self.total = sum(prod.precio_u * cant for prod, cant in self.productos)
        return self.total


    def mostrar_ticket(self):
        lineas = []
        lineas.append("       ACCESORIOS TECH ZONE      ")
        lineas.append("   ¡Gracias por preferirnos!    ")
        lineas.append("-" * 40)
        lineas.append(f"           TICKET #{self.numero_ticket}")
        lineas.append("-" * 40)
        lineas.append(f"Cliente: {self.cliente.nombre}")
        lineas.append(f"DUI: {self.cliente.Dui}")
        lineas.append(f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}")
        lineas.append("-" * 40)
        lineas.append(f"{'Producto':20} {'Cant':>4} {'Precio':>7} {'Subtot':>7}")
        lineas.append("-" * 40)

        for prod, cant in self.productos:
            subtotal = prod.precio_u * cant
            lineas.append(f"{prod.nombre[:20]:20} {cant:>4} ${prod.precio_u:>6.2f} ${subtotal:>6.2f}")

        lineas.append("-" * 40)
        lineas.append(f"{'TOTAL:':>32} ${self.calcular_total():>6.2f}")
        lineas.append("=" * 40)
        lineas.append("    ¡Gracias por su compra!    ")
        lineas.append("=" * 40)

        ticket_texto = "\n".join(lineas)
        print(ticket_texto)
        return ticket_texto

    def generar_ticket_pdf(self, carpeta="tickets"):
        os.makedirs(carpeta, exist_ok=True)
        archivo = os.path.join(carpeta, f"ticket_{self.numero_ticket}.pdf")
        c = canvas.Canvas(archivo, pagesize=letter)

        y = 270  
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(105*mm, y*mm, f"TICKET #{self.numero_ticket}")
        y -= 8

        c.setFont("Helvetica", 10)
        c.drawString(20*mm, y*mm, f"Cliente: {self.cliente.nombre}")
        y -= 5
        c.drawString(20*mm, y*mm, f"DUI: {self.cliente.Dui}")
        y -= 5
        c.drawString(20*mm, y*mm, f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M:%S')}")
        y -= 10

        c.setFont("Helvetica-Bold", 10)
        c.drawString(20*mm, y*mm, "Producto")
        c.drawRightString(150*mm, y*mm, "SubTotal")
        y -= 5
        c.line(20*mm, y*mm, 180*mm, y*mm)
        y -= 5

        c.setFont("Helvetica", 10)
        for prod, cant in self.productos:
            subtotal = prod.precio_u * cant
            texto = f"{prod.nombre[:30]} x{cant} (${prod.precio_u:.2f})"
            c.drawString(20*mm, y*mm, texto)
            c.drawRightString(150*mm, y*mm, f"${subtotal:.2f}")
            y -= 10

        y -= 5
        c.line(20*mm, y*mm, 180*mm, y*mm)
        y -= 7

        c.setFont("Helvetica-Bold", 11)
        c.drawRightString(150*mm, y*mm, f"TOTAL: ${self.calcular_total():.2f}")
        y -= 10

        c.setFont("Helvetica-Oblique", 10)
        c.drawCentredString(105*mm, y*mm, "¡Gracias por su compra!")

        c.save()
        print(f"Ticket guardado en: {archivo}")
        return archivo
