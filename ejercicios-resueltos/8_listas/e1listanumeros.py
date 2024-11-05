def manejar_lista():
    numeros = [1, 2, 3, 4, 5]
    
    # Agregar un número
    numeros.append(6)
    print("Lista después de agregar 6:", numeros)

    # Eliminar un número
    numeros.remove(3)
    print("Lista después de eliminar 3:", numeros)

    # Mostrar la longitud de la lista
    longitud = len(numeros)
    print("La longitud de la lista es:", longitud)

    # Acceder a un elemento específico
    primer_elemento = numeros[0]
    print("El primer elemento es:", primer_elemento)

# Llamar a la función
manejar_lista()
