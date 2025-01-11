# Poner en range el número de veces que queremos que se repita. Empieza en 0
for i in range(5):
    print("Contador: ", i)
    print("Contador: ", i + 1) # para que empiece en el 1

# Bucle para repetir una función X veces
def saludar():
    print("Hola")

for i in range(10):
    saludar()