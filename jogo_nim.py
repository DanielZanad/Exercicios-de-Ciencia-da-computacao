def main():
    while True:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("1 - para jogar uma partida isolada")
        escolha = int(input("2 - para jogar um campeonato "))
    
        if(escolha == 1):
            partida()
        elif(escolha == 2):
            campeonato()
        else:
            print("Digite um valor valido!")

        break
    
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1) == 0):
        print("Voce começa!")
    else:
        print("Computador começa!")
    while True:
        if (n % (m + 1) == 0):
            while n > 0:
                tirado = usuario_escolhe_jogada(n,m)
                n =  tirado
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else: 
                    print(f"Agora restam {n} peças no tabuleiro.")
                tirado = computador_escolhe_jogada(n,m)
                n = tirado
                if n == 0:
                    break
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print(f"Agora restam {n} peças no tabuleiro.")
                

        else:
            while n > 0:
                tirado = computador_escolhe_jogada(n,m)
                n = tirado
                if n == 0:
                    break
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else: 
                    print(f"Agora restam {n} peças no tabuleiro.")
                tirado = usuario_escolhe_jogada(n,m)
                n = tirado
                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else: 
                    print(f"Agora restam {n} peças no tabuleiro.")
               
        print("Fim do jogo! O computador ganhou!")

        break
    return 0

def computador_escolhe_jogada(n,m):
    
    for c in range(0, n+1):
        if (n - c) % (m + 1) == 0:
            if c == 1:
                print("O computador tirou uma peça.")
            else:
                print(f"O computador tirou {c} peça.")
            print(c)
            return n - c
        else:
            if m > n:
                while m > n:
                    m = m - 1
                print(f"O computador tirou {m} peças.")
                return n - m
            else:
                if m == 1:
                    print("O computador tirou uma peça.")
                    return n-m
                else:
                    print(f"O computador tirou {m} peças.")
                    return n - m

def usuario_escolhe_jogada(n,m):
    while True:
        tirar = int(input("Quantas peças você vai tirar? "))
        if tirar > m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            print(f"Voce tirou {tirar} peças.")    
            return n - tirar   

def campeonato():

    usuario = 0
    computador = 0


    for c in range(3):
        print(f"*** Rodada {c+1} ****")


        vencedor = partida()


        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1

    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))


main()    

