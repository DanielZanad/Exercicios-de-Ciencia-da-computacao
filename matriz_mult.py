def sao_multiplicaveis(matriz1: list, matriz2: list) -> bool:
    if len(matriz1[0]) == len(matriz2):
        return True
    else:
        return False

m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]

print(sao_multiplicaveis(m1, m2))

    