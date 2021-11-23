def primeiro_lex(listaNomes: list)-> str:
    menor = listaNomes[0]
    if len(listaNomes) == 1:  
        return menor
    for c in range(len(listaNomes)):
        if menor > listaNomes[c+1]:
            menor = listaNomes[c+1]
        if len(listaNomes)-1 == c+1:
            return menor


