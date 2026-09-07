# ==========================================
# 1. FUNCIÓN: Recibe datos, procesa y devuelve un resultado
# ==========================================
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal # Devuelve un valor para que pueda ser guardado en una variable

resultado = calcular_subtotal(45.50, 3)
print("Subtotal: C$", resultado)


# ==========================================
# 2. PROCEDIMIENTO: Realiza una acción (imprimir) sin usar return
# ==========================================
def mostrar_resumen(cliente, total):
    print("--- RESUMEN DE VENTA ---")
    print("Cliente:", cliente)
    print("Total: C$", total)
    # No tiene return, solo ejecuta acciones en pantalla.

mostrar_resumen("Ana López", 136.50)