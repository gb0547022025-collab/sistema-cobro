from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from datetime import datetime
import os

class TicketPDF:
    def __init__(self, ticket):
        self.ticket = ticket

    def generar_ticket(self):
        os.makedirs("tickets", exist_ok=True)
        ruta_pdf = f"tickets/ticket_{self.ticket.numero_ticket}.pdf"

        c = canvas.Canvas(ruta_pdf, pagesize=(80 * mm, 200 * mm))

        nombre_negocio = "ACCESORIOS TECH ZONE"
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(40 * mm, 190 * mm, nombre_negocio)  

        c.line(5 * mm, 188 * mm, 75 * mm, 188 * mm)

        c.setFont("Helvetica", 8)
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        c.drawString(5 * mm, 180 * mm, f"Ticket No: {self.ticket.numero_ticket}")
        c.drawString(5 * mm, 175 * mm, f"Cliente: {self.ticket.cliente.nombre}")
        c.drawString(5 * mm, 170 * mm, f"Fecha: {fecha}")


        y = 160 * mm
        c.setFont("Helvetica", 8)
        for prod, cant in self.ticket.productos:
            subtotal = prod.precio_u * cant
            c.drawString(5 * mm, y, f"{prod.nombre[:20]} x{cant}")
            c.drawRightString(75 * mm, y, f"${subtotal:.2f}")
            y -= 5 * mm

        c.setFont("Helvetica-Bold", 9)
        c.line(5 * mm, y - 2 * mm, 75 * mm, y - 2 * mm)
        y -= 7 * mm
        c.drawString(5 * mm, y, "TOTAL:")
        c.drawRightString(75 * mm, y, f"${self.ticket.calcular_total():.2f}")

        c.setFont("Helvetica-Oblique", 7)
        c.drawCentredString(40 * mm, y - 10 * mm, "¡Gracias por su compra!")

        c.showPage()
        c.save()
        print(f" Ticket generado en: {ruta_pdf}")

        try:
            os.startfile(ruta_pdf, "print")
            print("Enviando ticket a la impresora...")
        except Exception as e:
            print(" No se pudo imprimir automáticamente:", e)