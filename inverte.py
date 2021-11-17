lista = []
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        lista.append(n)
i = 0
c = -1
print()
while len(lista) > i:
    print(lista[c])
    c -= 1
    i += 1
print()