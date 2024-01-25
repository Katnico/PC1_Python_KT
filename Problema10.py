def eliminar_elementos(lista, posiciones):
    nueva_lista = list(lista)
    
    for posicion in sorted(posiciones, reverse=True):
        if 0 <= posicion < len(nueva_lista):
            nueva_lista.pop(posicion)
    
    return nueva_lista

lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

posiciones_a_eliminar = [0, 4, 5]

resultado = eliminar_elementos(lista_muestra, posiciones_a_eliminar)

print("Lista original:", lista_muestra)
print("Resultado después de eliminar posiciones:", resultado)