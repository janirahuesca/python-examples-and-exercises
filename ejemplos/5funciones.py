# Definimos una función sin parámetros
def saludar():
    print("Hola buenos días")

# Definimos funciones que reciben parámetros y devolvemos un valor
def saludar_con_nombre(nombre):
    saludo = "Hola " + nombre
    return saludo

# Llamamos a la función saludar
saludar()

# Llamamos a la función saludar con nombre
nombre = input("Introduce tu nombre:")
saludo = saludar_con_nombre(nombre)
print(saludo)

nombre2 = input("Introduce tu nombre:")
saludo2 = saludar_con_nombre(nombre2)
print(saludo2)
