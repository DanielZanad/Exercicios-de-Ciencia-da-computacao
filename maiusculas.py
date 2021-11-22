def maiusculas(palavra: str)-> str: 
    resultado = ""
    palavra = palavra.replace(" ", "")
    for c in range(len(palavra)):
        if palavra[c] < '[':
            if palavra[c].isalpha():
                resultado += palavra[c]
    return resultado

print(maiusculas('HELLO WORLD'))
