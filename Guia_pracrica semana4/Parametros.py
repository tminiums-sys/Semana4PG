def aplicar_aumento(precio):
    # Aquí intentamos modificar el parámetro reasignándolo
    precio = precio + 100
    print("Precio dentro:", precio)

precio_producto = 500
aplicar_aumento(precio_producto)

# Al imprimir afuera, el valor NO cambia y sigue siendo 500. ¿Por qué?
print("Precio fuera:", precio_producto)