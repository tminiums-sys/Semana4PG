def calcular_pago(horas, tarifa):
    # 'pago' es una variable local. Solo vive y existe dentro de esta función.
    pago = horas * tarifa
    print("Pago dentro de la función: C$", pago)
# Llamamos a la función correctamente:
calcular_pago(40, 120)
# EXPLICACIÓN DE LO QUE ESTaría MAL (ERROR):
# Si intentas ejecutar la siguiente línea fuera de la función:
# print(pago)
# Python arrojará un NameError. ¿Por qué? Porque la variable 'pago' 
# muere al terminar la función y no existe en el ámbito global del programa.