anterior = -1
achou = False
numero = int(input('Digite um número inteiro: '))
while numero != 0 :
    valor = numero %  10
    if valor == anterior:
        achou = True
        break
    else: 
        achou = False
    anterior = valor
    numero = numero // 10
if achou:
    print('sim')
else:
    print('não')