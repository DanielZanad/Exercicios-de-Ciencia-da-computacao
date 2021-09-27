def soma_elementos(lista):
    resultado = 0
    for c in lista:
        resultado += c
    return resultado


soma = soma_elementos([2,3,2,2])
print(soma)