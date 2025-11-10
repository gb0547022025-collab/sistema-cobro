from ClienteRepository import ClienteRepository
from ProductoRepository import ProductoRepository
from VentaRepository import VentaRepository
from LectorCodigo import LectorCodigo
from ticket import Ticket
from venta import Venta
from sistema import Sistema


repo_clientes = ClienteRepository()
repo_clientes.cargar_desde_archivo()

repo_productos = ProductoRepository()
repo_productos.generar_codigos_barras() 

lector = LectorCodigo(repo_productos.get_dict())
repo_ventas = VentaRepository()

dui = input("Ingrese el DUI del cliente: ")
nombre = input("Ingrese el nombre del cliente: ").strip()
cliente = repo_clientes.registrar_si_no_existe(nombre, dui)

numero_ticket = repo_ventas.generar_numero_ticket()

ticket = Ticket(numero_ticket, cliente)
venta = Venta(lector, ticket)

sistema = Sistema(venta, repo_ventas, repo_productos)
sistema.ejecutar()

repo_ventas.guardar_en_archivo()
repo_clientes.guardar_en_archivo()


