def ordenada(lista: list)-> bool:
    if lista[0] >= lista[len(lista)-1]:
        for i in range(len(lista)-1):
            if len(lista) > 1:
                if lista[i] < lista[i+1]:
                    return False
    elif lista[0] <= lista[len(lista)-1]:
        for i in range(len(lista)-1):
            if len(lista) > 1:
                if lista[i] > lista[i+1]:
                    return False
    return True

print(ordenada([5,4,3,5]))