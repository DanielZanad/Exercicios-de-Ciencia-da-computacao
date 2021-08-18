def maximo(n1,n2,n3):
    n = [n1,n2,n3]
    maior = n1
    for x in n:
        if x > maior:
            maior = x
    return maior

