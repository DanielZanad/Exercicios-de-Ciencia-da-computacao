import math


def maior_primo(n):

    raiz = int(math.sqrt(n))
    for d in range(2, raiz +1):
        if n % d == 0:
            return maior_primo(n-1)
    return n