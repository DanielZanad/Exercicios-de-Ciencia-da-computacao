def conta_letras(frase: str, contar="vogais" ):
    aux = frase.split()
    frase = ""
    for c in range(len(aux)):
        frase += aux[c]
    resultado = vogais_consoantes(frase)
    if contar == "vogais":
        return resultado[0]
    else:
        return resultado[1]


def vogais_consoantes(frase: str):
    vogais = 0
    consoantes = 0
    for c in range(len(frase)):
        if frase[c].isalpha():
            if frase[c].lower() in ['a', 'e','i', 'o', 'u']:
                vogais += 1
            else:
                consoantes += 1
    resultado = [vogais, consoantes]
    return resultado
