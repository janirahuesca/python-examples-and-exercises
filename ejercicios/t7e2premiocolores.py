# Función para pedir al usuario que introduzca un color:
def solicitar_color():
    color = input("Introduce un color: ")
    return color.lower()  # Convertimos a minúsculas para evitar errores con mayúsculas

# Función para comprobar si color introducido es el "azul" y dar el mensaje oportuno
def comprobar_color(color):
    if(color == "azul"):
        mensaje = "El premio ha sido conseguido"
    else:
        mensaje = "No se ha ganado el premio"
    return mensaje

# Realizar la acción de solicitar el color 5 veces
premio_conseguido = False  # Variable para saber si ya se consiguió el premio

for i in range(5):
    color = solicitar_color()  # Llamar a la función para obtener el color del usuario
    mensaje = comprobar_color(color)  # Comprobar el color y obtener el mensaje
    print(mensaje)  # Mostrar el mensaje

    if color == "azul":  # Si el color es azul, ya no hace falta seguir pidiendo colores
        premio_conseguido = True
        break  # Salir del bucle si se ha conseguido el premio

# Mostrar mensaje de premio solo si no se consiguió "azul"
if not premio_conseguido:
    print("No se ha ganado el premio.")