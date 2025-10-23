import random

def criar_campo(linha, coluna):
    """Cria um matriz com as dimensões fornecidas."""

    mapa = [[' ' for _ in range(coluna)] for _ in range(linha)] #Cria uma matriz vazia
    return mapa


def desenha_campo(mapa):
    """Preenche as bordas do mapa com '-' e '|'. e o interior com '*'."""

    linha = len(mapa) 
    coluna = len(mapa[0]) 

    for i in range(linha):
        for j in range(coluna):
            if i == 0 or i == linha - 1: 
                mapa[i][j] = '-' #Preenche as bordas superior e inferior
            elif j == 0 or j == coluna - 1: 
                mapa[i][j] = '|' #Preenche as bordas da esquerda e direita
            else: 
                mapa[i][j] = '*' #Preenche o interior do mapa
    return mapa


def alocar_bombas(mapa, qtd_bombas):
    """Aloca as bombas no mapa."""

    linha = len(mapa)
    coluna = len(mapa[0])
    bombas_colocadas = 0

    while bombas_colocadas < qtd_bombas: #Loop até que todas as bombas sejam alocadas
        x = random.randint(1, linha - 2)
        y = random.randint(1, coluna - 2)

        if mapa[x][y] != 'B': #Verifica se já existe uma bomba na posição
            mapa[x][y] = 'B' 
            bombas_colocadas += 1


def desenhar_campo(mapa):
    """Mostra o mapa na tela."""

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print(mapa[i][j], end=" ")
        print()


if __name__ == "__main__":

    print("\n\t==== CAMPO MINADO ====\n")


    while True: #Pede a dimensão do campo ao usuário
        dimensao = int(input("\nDigite a dimensão do campo minado (MÁX: 10): ")) 
        if dimensao > 10:
            print("Dimensão invalida! Digite novamente.")
        elif dimensao < 1:
            print("Dimensão invalida! Digite novamente.")
        else:
            break

    mapa_real = criar_campo(dimensao + 2, dimensao + 2) #Cria o mapa real com bordas
    mapa_visivel = criar_campo(dimensao + 2, dimensao + 2) #Cria o mapa visível ao usuario com bordas

    desenha_campo(mapa_real) #Preenche as bordas e o interior do mapa real
    desenha_campo(mapa_visivel) #Preenche as bordas e o interior do mapa visível

    while True: #Pede a quantidade de bombas ao usuário
        qtd_bombas = int(input(f"Digite o número de bombas (MÁX: {format(dimensao * dimensao - 1)}): "))
        if qtd_bombas > dimensao * dimensao - 1:
            print("Número de bombas inválido! Digite novamente.")
        elif qtd_bombas < 1:
            print("Número de bombas inválido! Digite novamente.")
        else:
            break

    alocar_bombas(mapa_real, qtd_bombas) #Aloca as bombas no mapa real
    desenhar_campo(mapa_visivel) #Mostra o mapa visível ao usuário


    while True: #Loop principal do jogo
        print("Qual operação deseja realizar?")
        print("1 - Revelar uma posição")
        print("2 - Marcar/Desmarcar uma bandeira")
        print("0 - Sair do jogo")

        opcao = int(input("Digite a opção desejada: "))
       
        if opcao == 1:
            x = int(input("Digite a linha que deseja revelar: "))
            y = int(input("Digite a coluna que deseja revelar: "))
            # Lógica para revelar a posição (a ser implementada)
        elif opcao == 2:
            x = int(input("Digite a linha da bandeira: "))
            y = int(input("Digite a coluna da bandeira: "))
            # Lógica para marcar/desmarcar bandeira (a ser implementada)
        elif opcao == 0:
            print("Saindo do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")
