import math
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
delta = b ** 2 - 4 * a * c

if delta == 0:
    print(f'a raiz desta equação é {delta}')
else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        raizDelta = math.sqrt(delta)
        x1 = (raizDelta+(-b))/(2*a)
        x2 = (raizDelta-(-b))/(2*a)
        if(x1 < x2):
            print(f'as raízes da equação são {x1} e {x2}')
        else:
            print(f'as raízes da equação são {x2} e {x1}')