from crud import registrar, mostrar


def main():
    while True:
        print("\n1. Registrar  2. Mostrar  3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar("Persona", int(input("Edad: ")))
        elif opcion == "2":
            mostrar()
        elif opcion == "3":
            break
        else:
            print("No válida")


if __name__ == "__main__":
    main()
