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

print(soma_matrizes([[1,2,3], [4,5,6], [7,8,9]], [[10,20,30], [40,50,60], [70,80,90]]))