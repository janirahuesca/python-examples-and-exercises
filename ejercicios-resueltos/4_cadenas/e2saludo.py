nombre = input("¿Cuál es tu nombre? ")
saludo = "Hola, " + nombre + "!"
longitud = len(saludo)
mayusculas = saludo.upper()
minusculas = saludo.lower()
reemplazo = saludo.replace("Hola", "Adios")

print(saludo)
print("Longitud:", longitud)
print("Texto en mayúsculas:", mayusculas)
print("Texto en minúsculas:", minusculas)
print("Texto reemplazado:", reemplazo)

