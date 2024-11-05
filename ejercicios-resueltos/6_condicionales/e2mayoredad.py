def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad."
    else:
        return "Eres menor de edad."

# Solicitar la edad al usuario
edad_usuario = int(input("Ingresa tu edad: "))
resultado = es_mayor_de_edad(edad_usuario)
print(resultado)
