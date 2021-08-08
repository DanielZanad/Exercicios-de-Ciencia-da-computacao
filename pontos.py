import math

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um outro numero: '))
n3 = int(input('Digite um outro numero: '))
n4 = int(input('Digite um outro numero: '))

d = math.sqrt((n1 - n3)**2 + (n2 - n4)**2)
if (d >= 10):
    print('longe')
else:
    print('perto')

