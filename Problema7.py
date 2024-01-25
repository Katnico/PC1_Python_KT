def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

while True:
    try:
        Primernumero = float(input("Ingrese el primer número: "))
        Segundonumero = float(input("Ingrese el segundo número: "))

        print("\nMenú:")
        print("1. Mostrar suma de los dos números")
        print("2. Mostrar resta (primer número menos segundo número)")
        print("3. Mostrar multiplicación de los dos números")
        print("0. Salir")

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            print("La suma es:", suma(Primernumero, Segundonumero))
        elif opcion == 2:
            print("La resta es:", resta(Primernumero, Segundonumero))
        elif opcion == 3:
            print("La multiplicación es:", multiplicacion(Primernumero, Segundonumero))
        elif opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")

    except ValueError:
        print("Error: Ingrese números válidos.")