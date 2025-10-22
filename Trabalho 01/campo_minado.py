def criar_mapa(linha, coluna):
    """Cria um matriz com as dimensões fornecidas."""

    mapa = [[' ' for _ in range(coluna)] for _ in range(linha)]
    return mapa


def bordas_mapa(mapa):
    """Preenche as bordas do mapa com '-' e '|'. e o interior com '*'."""

    linha = len(mapa)
    coluna = len(mapa[0])

    for i in range(linha):
        for j in range(coluna):
            if i == 0 or i == linha - 1:
                mapa[i][j] = '-'
            elif j == 0 or j == coluna - 1:
                mapa[i][j] = '|'
            else:
                mapa[i][j] = '*'
    return mapa


def desenhar_campo(mapa):
    """Mostra o mapa na tela."""
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print(mapa[i][j], end=" ")
        print()


if __name__ == "__main__":
    while True:
        dimensao = int(input("Digite a dimensão do campo minado (MÁX: 10): "))
        if dimensao > 10:
            print("Dimensão invalida! Digite novamente")
        elif dimensao < 1:
            print("Dimensão invalida! Digite novamente")
        else:
            break

        

    # Cria o mapa e adiciona bordas
    mapa = criar_mapa(dimensao + 2, dimensao + 2)
    mapa = bordas_mapa(mapa)

    print("\n=== Campo Minado ===\n")
    desenhar_campo(mapa)

