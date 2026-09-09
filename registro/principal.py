import crud

def leerDatos():
    print("Dime la nota: ")
    nota = int(input())
    crud.agregar(nota)

def menu():
    print(""""
1. Ingresar nota
2. Mostrar notas
3. Evaluar notas
0. Salir
Digite una opcion valida:
""")
    opcion = int(input())
    return opcion

def main():
    while True:
        op = menu()
        if op == 1:
            leerDatos()
        elif op ==2:
            print(crud.mostrar())
        elif op ==3:
            crud.evaluarNotas()
        elif op ==0:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, intente de nuevo")
            
main() 