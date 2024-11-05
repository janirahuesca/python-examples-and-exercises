def calcular_area(base, altura):
    return (base * altura) / 2

base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = calcular_area(base, altura)
print("El área del triángulo es:", area)
