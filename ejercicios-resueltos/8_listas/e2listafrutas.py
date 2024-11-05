def manejar_lista_palabras():
    palabras = ["manzana", "banana", "cereza", "durazno", "kiwi"]
    
    # Agregar una palabra
    palabras.append("mango")
    print("Lista después de agregar 'mango':", palabras)

    # Eliminar una palabra
    palabras.remove("banana")
    print("Lista después de eliminar 'banana':", palabras)

    # Mostrar la longitud de la lista
    longitud = len(palabras)
    print("La longitud de la lista es:", longitud)

    # Acceder a un elemento específico
    primer_elemento = palabras[0]
    print("El primer elemento es:", primer_elemento)

# Llamar a la función
manejar_lista_palabras()
