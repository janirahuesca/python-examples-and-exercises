# Función para solicitar los datos al usuario
def solicitar_color():
    color = input("Elige un color entre los siguientes (Rojo, Verde, Azul, Amarillo, o Morado): ").capitalize() # para asegurar que el formato del color introducido sea consistente (primer carácter en mayúscula)
    return color

# Función para devolver un mensaje concreto según el color itroducido por el usuario
def mensaje_segun_color(color):
    if (color == "Rojo"):
        mensaje = "El rojo es el color de la pasión y la energía. ¡Hoy será un día lleno de acción y emoción! No temas a los desafíos, saldrás victorioso."
    elif(color == "Verde"):
        mensaje = "El verde representa la esperanza y el crecimiento. Algo nuevo y positivo está por florecer en tu vida. Confía en los pequeños cambios que te acercan a tus metas."
    elif(color == "Azul"):
        mensaje = "El azul simboliza la calma y la serenidad. Hoy estarás rodeado de tranquilidad y equilibrio. Aprovecha este momento para reflexionar y renovar tu energía."
    elif(color == "Amarillo"):
        mensaje = "El amarillo es el color de la felicidad y el optimismo. ¡Prepárate para un día lleno de alegría y buenas noticias! Alguien cercano te sorprenderá de forma positiva."
    elif(color == "Morado"):
        mensaje = "El morado evoca la sabiduría y la creatividad. Hoy te sentirás inspirado y lleno de ideas. Es el momento ideal para dejar volar tu imaginación y tomar decisiones importantes."
    else:
        mensaje = "Color incorrecto"
    return mensaje

# Pedir al usuario que elija un color
color = solicitar_color()

# Llamar a la función de mensaje_segun_color
mensaje = mensaje_segun_color(color)

# Imprimir el mensaje
print(mensaje)