# Función para pedir datos
def pedir_datos(datos):
    dato_solicitado = input(datos)
    return dato_solicitado

# Función para calcular precio total
def calcular_total(precio, cantidad, descuento, iva):
    total_bruto = precio * cantidad
    total_descuento = total_bruto * (descuento/100)
    subtotal = total_bruto - total_descuento
    total_iva = subtotal * (iva/100)
    total = subtotal + total_iva
    return total

# Solicitamos los datos del producto
nombre = pedir_datos("Nombre del producto: ")
precio_unidad = float(pedir_datos("Precio por unidad del producto: "))
cantidad = int(pedir_datos("Cantidad de productos que desea comprar: "))
descuento = float(pedir_datos("Descuento en porcentaje: "))
iva = float(pedir_datos("IVA en porcantaje: "))

# Imprimimos los datos solicitados
print(f"Producto: {nombre}")
print(f"Precio por unidad: {precio_unidad:.2f} €")
print(f"Cantidad: {cantidad}")
print(f"Descuento: {descuento:.2f} %")
print(f"IVA: {iva:.2f} %")

# Realizar el cálculo del precio total aplicando el descuento y el IVA
total = calcular_total(precio_unidad, cantidad, descuento, iva)

# Mostrar el precio total
print(f"El precio total de la compra es: {total:.2f} €")