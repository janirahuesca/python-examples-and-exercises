# Definimos funcion
def nota_final(nota):
    if (nota > 8):
        mensaje = "SOBRESALIENTE"
    elif (nota < 5):
        mensaje = "SUSPENSO"
    else:
        mensaje = "APROBADO"
    return mensaje

# Pedir a usuario que introduzca la nota
nota = float(input("Introduce tu nota del examen: "))

# Llamamos a la función para que nos diga el mensaje
mensaje = nota_final(nota)

# Imprimir el mensaje con la nota final
print(mensaje)