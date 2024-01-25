def invertir_lista(lista):
    lista_invertida = list(lista)
    lista_invertida.reverse()
    return lista_invertida

mi_lista = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = invertir_lista(mi_lista)

print("Lista original:", mi_lista)
print("Lista invertida:", lista_invertida)