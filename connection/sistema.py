import sys

from product_dao import ProductDAO
from product import Producto

class banner:

    def mostrar_banner(self):
        print("*********************************")
        print("*                               *")
        print("*    Bienvenido a Cafetería 404 *")
        print("*                               *")
        print("*********************************")


    def mostrar_menu(self):
        print("\n----------- MENÚ -----------")
        print("1. Realizar pedido")
        print("2. Acerca de")
        print("3. Administrar productos")
        print("4. Salir")

    def realizar_pedido(self):
        print("Realizando pedido...\n")

        # Obtener la lista de productos desde la base de datos
        lista_productos = ProductDAO.seleccionar()

        # Mostrar los productos disponibles
        print("Productos disponibles:")
        for i, producto in enumerate(lista_productos, start=1):
            print(f"{i}. {producto.nombre} - ${producto.precio}")

        pedido = []  # Lista para almacenar los productos del pedido
        opciones = len(lista_productos)

        while True:
            # Solicitar al usuario que elija un producto
            seleccion = int(
                input(f"\nSelecciona el número de producto que deseas ordenar: ({opciones+1} para salir): "))
            if seleccion == (opciones+1):
                break  # El usuario ha elegido salir del programa

            if seleccion < 1 or seleccion > len(lista_productos):
                print("Selección inválida.")
                continue

            producto_seleccionado = lista_productos[seleccion - 1]
            print(
                f"\nHas seleccionado: {producto_seleccionado.nombre} - ${producto_seleccionado.precio}\n")

            # Solicitar al usuario que ingrese la cantidad
            cantidad = int(input("Ingresa la cantidad: "))
            if cantidad <= 0:
                print("Cantidad inválida.")
                continue

            # Agregar el producto y la cantidad al pedido
            pedido.append((producto_seleccionado, cantidad))

        # Mostrar el resumen del pedido
        if pedido:
            print("\nResumen del pedido:")
            total = 0
            for producto, cantidad in pedido:
                subtotal = producto.precio * cantidad
                total += subtotal
                print(
                    f"{producto.nombre} - ${producto.precio} x {cantidad} = ${subtotal}")

            print(f"\nTotal a pagar: ${total}")

            # Solicitar al usuario que ingrese la cantidad con la que pagará
            pago = float(input("\nIngrese la cantidad con la que pagará: "))
            if pago < total:
                print("El monto ingresado es insuficiente.")
            else:
                cambio = pago - float(total)
                print(f"Cambio a devolver: ${cambio}")
        else:
            print("No se agregaron productos al pedido.")

        def acerca_de(self):

            nombres = """Ahumada, Brian; Alancay, Abel Matías; Alsina, Maximiliano; Berrini, 
                   Alejandro; Calle, Sonia; Chávez, Rodrigo; Costa, María Eugenia; Navarro, Lucas; Sanguinetti, Pablo"""
            print("Lista de nombres:")
            print(nombres)

        def salir(self):
            print("¡Hasta luego!")
            sys.exit()
