
class Sistema:
    def __init__(self, venta, repo_ventas, repo_productos):
        self.venta = venta
        self.repo_ventas = repo_ventas
        self.repo_productos = repo_productos

    def mostrar_menu(self):
        print("\n====== MENÚ ======")
        print("1. Escanear producto")
        print("2. Agregar al ticket")
        print("3. Finalizar compra")
        print("4. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                codigo = input("Ingrese código de producto: ")
                producto = self.venta.escanear_producto(codigo)
                if producto:
                    print(producto)
            elif opcion == "2":
                codigo = input("Código: ")
                cantidad = int(input("Cantidad: "))
                if self.repo_productos.actualizar_stock(codigo, cantidad):
                    self.venta.agregar_al_ticket(codigo, cantidad)
                    print("Producto agregado al ticket y stock actualizado.")
                else:
                    print(" No se pudo agregar. Stock insuficiente o código inválido.")

            elif opcion == "3":
                self.venta.finalizar_compra(self.repo_ventas)
                break
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")
