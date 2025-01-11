# Guardar los productos y los precios de los productos que tiene la tienda
camiseta = float(10)
sudadera = float(20.5)
gorra = float(5.5)

# Pedir a usuario que introzca la cantidad que quiere de cada producto
cantidad_camisetas = int(input("Número de camisetas: "))
cantidad_sudaderas = int(input("Número de sudaderas: "))
cantidad_gorras = int(input("Número de gorras: "))

# Mostrar total compra sumando el 21% de IVA
# Calcular el total de cada artículo según la cantidad
total_camisetas = cantidad_camisetas * camiseta
total_sudaderas = cantidad_sudaderas * sudadera
total_gorras = cantidad_gorras * gorra

# Calcular el total de la compra sin IVA
total_compra = (total_camisetas + total_sudaderas + total_gorras)

# Calcular el IVA (21% del total de la compra sin IVA)
iva = total_compra * 0.21

# Calcular el total con IVA
total_con_iva = total_compra + iva

# Mostrar el resultado
print("El precio total de la compra, incluyendo el 21% de IVA, es de", total_con_iva, "€.")