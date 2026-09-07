def calcular_subtotal (precio_unitario, cantidad):
    return precio_unitario * cantidad

def calcular_descuento (subtotal):
    if subtotal >= 3000:
        return subtotal * 0.08
    return 0.0

def calcular_iva (subtotal):
    return subtotal * 0.16

def calcular_total (subtotal, descuento, iva):
    return subtotal - descuento + iva

def mostrar_factura (precio_unitario, cantidad, descuento, iva, subtotal, total):
    print("factura de compra. ")
    print(f"precio unitario: {precio_unitario}")
    print(f"cantidad: {cantidad}")
    print(f"descuento: {descuento}")
    print(f"iva: {iva}")
    print(f"subtotal: {subtotal}")
    print(f"total: {total}")

nombre_prducto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = calcular_subtotal(precio_unitario, cantidad)
descuento = calcular_descuento(subtotal)
iva = calcular_iva(subtotal)
total = calcular_total(subtotal, descuento, iva)    

print ("---------------------------------")
mostrar_factura(precio_unitario, cantidad, descuento, iva, subtotal, total)