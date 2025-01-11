# Guardar la frase introducida por el usuario
frase = input("Introduce una frase:")

# Longitud de la frase
longitud = len(frase.strip()) # Elimina los espacios al principio y al final de la cadena

# Frase en mayúsculas
frase_may = frase.upper()

# Frase en minúsculas
frase_min = frase.lower()

# Imprimir por consola los valores de la frase que hemos manipulado
print("Longitud:", longitud)
print(frase_may)
print(frase_min)