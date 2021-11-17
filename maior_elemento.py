def maior_elemento(lista):
    maior = lista[0]
    for c in lista:
        if c > maior:
            maior = c
    
    return maior

print(maior_elemento([2,3,4,3,10,5]))