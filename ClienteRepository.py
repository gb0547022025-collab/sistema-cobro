from Cliente import Cliente
import csv

class ClienteRepository:
    def __init__(self):
        self.clientes = []

    def buscar_por_dui(self, dui):
        for cliente in self.clientes:
            if cliente.Dui == dui:
                return cliente
        return None

    def cargar_desde_archivo(self, ruta="clientes.csv"):
        try:
            with open(ruta, mode="r", encoding="utf-8") as archivo:
                reader = csv.reader(archivo)
                for fila in reader:
                    if len(fila) == 2:
                        nombre, dui = fila
                        self.clientes.append(Cliente(nombre, dui))
        except FileNotFoundError:
            print("Archivo de clientes no encontrado, se creará uno nuevo.")

    def registrar_si_no_existe(self, nombre, dui):
        cliente = self.buscar_por_dui(dui)
        if cliente:
            print(f"Cliente ya registrado: {cliente.nombre}")
            return cliente
        else:
            nuevo = Cliente(nombre, dui)
            self.clientes.append(nuevo)
            print(f"Nuevo Cliente registrado: {nuevo.nombre}")
            return nuevo

    def guardar_en_archivo(self, ruta="clientes.csv"):
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            for c in self.clientes:
                writer.writerow([c.nombre, c.Dui])
