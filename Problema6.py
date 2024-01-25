edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio_entrada = 0 
elif edad>=4 and edad<=18:
    precio_entrada = 5 
else:
    precio_entrada = 10

print(f"El precio de la entrada es: ${precio_entrada}")