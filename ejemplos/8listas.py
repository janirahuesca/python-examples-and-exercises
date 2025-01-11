# Lista de notas
notas = [4, 6, 8, 10]

# Lista de nombres
nombres = ["Janira", "Jordi", "Neo", "Lola"]

# Agregar elemento al final de la lista
nombre = input("Introduce un nombre: ")
nombres.append(nombre) # el nombre introducido por el usuario
nombres.append("Mixi") # el nombre directamente

notas.append(11)

# Imprimir las listas
print(notas)
print(nombres)

# Eliminar un elemento de la lista
nota_a_eliminar = float(input("Introduce la nota a eliminar: "))
notas.remove(nota_a_eliminar) # la nota introducida por el usuario
nombres.remove("Mixi") # el nombre introducido por el usuario

# Imprimir de nuevo las listas para ver los cambios
print(notas)
print(nombres)

# Acceder a elementos según la posición
print("Alumno en la posición 2:", nombres[1])