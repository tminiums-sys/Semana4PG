nombre_empresa = "Tecnología Global S.A."

def mostrar_empresa():
    print("Nombre de la empresa:", nombre_empresa)

mostrar_empresa()


def calcular_total():
    total = 1500 
    print("Total dentro de la función:", total)

calcular_total()


contador_visitas = 0

def incrementar_visita():
    global contador_visitas
    contador_visitas += 1
    print("Visita registrada. Total actual:", contador_visitas)

incrementar_visita()
incrementar_visita()