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
