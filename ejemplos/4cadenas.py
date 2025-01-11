# Guradamos la ciudad de residencia del usuario
ciudad = input("Introduce la ciudad donde resides: ")

# Concatenar 2 cadenas
bienvenida = "Bienvenidos a " + ciudad

# Obtener el número de caracteres de la cadena
longitd = len(bienvenida)

# Convertir la cadena a mayuscúlas
bienvenida_mayusculas = bienvenida.upper()

# Convertir la cadena a minúsculas
bienvenida_minusculas = bienvenida.lower()

# Imprimir los diferentes valores
print(bienvenida)
print("Longitud:", longitd)
print(bienvenida_mayusculas)
print(bienvenida_minusculas)