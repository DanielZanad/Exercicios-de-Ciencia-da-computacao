def imprime_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == len(matriz[0])-1:
                print(str(matriz[i][j]))
            else:
                print(matriz[i][j], end=" ")


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)