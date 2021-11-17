def soma_matrizes(matriz: list, matriz2: list) -> any:
    if (len(matriz) + len(matriz[0])) != (len(matriz2) + len(matriz2[0])):
        return False
    else:
        result = []
        for i in range(len(matriz)): # numero de linhas
            linha = []
            for j in range(len(matriz[0])): # numero de colunas
                linha.append(matriz[i][j] + matriz2[i][j])        
            result.append(linha)
        return result

