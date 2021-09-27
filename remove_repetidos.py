def remove_repetidos(lista):
    lista2 = []
    for c in lista:
        if c not in lista2:
            lista2.append(c)
    lista2.sort()
    return lista2




lista = remove_repetidos([2,4,2,2,3,3,1])
print(lista)    