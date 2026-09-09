registros = []


def categoria_edad(edad):
    if edad <= 12:
        return "niño"
    if edad <= 25:
        return "joven"
    if edad <= 60:
        return "adulto"
    return "anciano"


def registrar(nombre, edad):
    registros.append([nombre, edad, categoria_edad(edad)])


def mayor_edad():
    if not registros:
        return ""

    mayor = registros[0]
    for r in registros[1:]:
        if r[1] > mayor[1]:
            mayor = r
    return f"{mayor[0]} con {mayor[1]} años"


def mostrar():
    for i, r in enumerate(registros, 1):
        print(i, r[0], r[1], "años", r[2])

    if registros:
        print("\nEl mayor es:", mayor_edad())
    else:
        print("No hay registros para comparar.")


def actualizar(i, nombre, edad):
    registros[i - 1] = [nombre, edad, categoria_edad(edad)]
