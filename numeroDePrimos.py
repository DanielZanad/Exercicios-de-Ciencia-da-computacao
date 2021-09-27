def n_primos(x):
    c = 0
    while x > 0:
        fator = 2
        while x % fator != 0 and fator <= x/2:
            fator = fator + 1
        if x % fator != 0:
            c += 1 
        x -= 1
    return c

print(n_primos(121))