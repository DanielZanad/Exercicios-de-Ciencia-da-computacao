def menor_nome(nomes: list)-> str:
    menor = nomes[0]
    for i in range(len(nomes)):   
        if len(nomes[i].strip()) < len(menor.strip()):
            menor = nomes[i]
    resultado = menor.strip()
    return resultado.capitalize()




