def numero_mayor(num1, num2):
    if num1 > num2:
        print("El número " + str(num1) + " es mayor que " + str(num2))
    elif num1 == num2:
        print("Los números son iguales.")
    else:
        print("El número " + str(num2) + " es mayor que " + str(num1))

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero_mayor(numero1, numero2)

