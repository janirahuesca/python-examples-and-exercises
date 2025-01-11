# Crear lista con 8 planetas del sistema solar
planetas = ["Mercurio", "Venus", "La Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# Función para solicitar un número al usuario
def solicitar_numero():
    numero = int(input("Introduce un número del 1 al 8: "))
    return numero

def comprobar_numero(numero):
    if(numero >= 1 and numero <= 8): # Verificamos si el número está dentro del rango 1-8
        indice = numero - 1
        print(f"El planeta {numero} es: {planetas[numero - 1]}. Se encuentra en el índice {indice}") 
    else:
        print("Número inválido, introduce un número entre 1 y 8") 
        
# Solicitamos el número
numero = solicitar_numero()

# Mostrar el planeta correspondiente
comprobar_numero(numero)