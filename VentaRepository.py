import csv
import os

class VentaRepository:
    def __init__(self):
        self.ventas = []
        self.archivo_contador = "tickets/contador.txt"
        os.makedirs("tickets", exist_ok=True)
        self._cargar_contador()

    def _cargar_contador(self):
        """Carga el número de ticket más reciente del archivo."""
        if os.path.exists(self.archivo_contador):
            with open(self.archivo_contador, "r") as f:
                contenido = f.read().strip()
                self.contador = int(contenido) if contenido else 0
        else:
            self.contador = 0

    def _guardar_contador(self):
        """Guarda el número de ticket actual."""
        with open(self.archivo_contador, "w") as f:
            f.write(str(self.contador))

    def generar_numero_ticket(self):
        """Genera el siguiente número de ticket de forma incremental y persistente."""
        self.contador += 1
        self._guardar_contador()
        return self.contador

    def guardar_venta(self, venta):
        """Guarda la venta actual en memoria."""
        self.ventas.append(venta)
        print(f"Venta registrada: Ticket #{venta.ticket_actual.numero_ticket}")

    def guardar_en_archivo(self, ruta="ventas.csv"):
        """Guarda todas las ventas en un archivo CSV."""
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            for v in self.ventas:
                writer.writerow([
                    v.ticket_actual.numero_ticket,
                    v.ticket_actual.cliente.nombre,
                    v.ticket_actual.cliente.Dui,
                    v.ticket_actual.total
                ])
