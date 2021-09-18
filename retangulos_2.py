n1 = int(input('digite a largura: '))
n2 = int(input('digite a altura: '))
c = 1
x = n2
while n2 > 0:
    if c == 1:
        print("#" * n1)
    elif c != 1 and c != x:
        print("#"," " * (n1 - 4), "#")
    elif c == x:
        print("#" * n1)
    c += 1
    n2 -= 1