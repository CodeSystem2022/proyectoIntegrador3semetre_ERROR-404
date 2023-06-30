from sistema import banner

def main(self):
    banner.mostrar_banner(self)

    while True:
        banner.mostrar_menu(self)
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            banner.realizar_pedido(self)
        elif opcion == "2":
            banner.acerca_de(self)
        elif opcion == "3":
            banner.menu_sistema(self)

        elif opcion == "4":
            banner.salir(self)
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.\n")


if __name__ == '__main__':
    main(1)