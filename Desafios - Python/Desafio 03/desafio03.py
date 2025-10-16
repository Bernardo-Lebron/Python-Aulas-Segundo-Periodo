labirinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'R', '-', '-', '#', '-', '-', '-', '#'],
    ['#', '-', '#', '-', '-', '-', '#', '-', '#'],
    ['#', '-', '-', '-', '#', '-', '-', '-', '#'],
    ['#', '#', '-', '#', '-', '-', '-', 'S', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

posicao_x = -1
posicao_y = -1

#Procura a posição inicial do robô
for y in range(len(labirinto)):
    for x in range(len(labirinto[y])):
        if labirinto[y][x] == 'R':
            posicao_x = x
            posicao_y = y

while True:
    #Imprime o labirinto
    for linha in labirinto:
        print(" ".join(linha))
    print("\nUse as teclas W, A, S, D para mover.")
    print("Seu objetivo é chegar em 'S'.\n")

    movimento = input("Qual movimento deseja realizar? ").lower()

    proxima_x = posicao_x
    proxima_y = posicao_y

    if movimento == 'a':
        proxima_x -= 1
    elif movimento == 'd':
        proxima_x += 1
    elif movimento == 'w':
        proxima_y -= 1
    elif movimento == 's':
        proxima_y += 1
    else:
        print("Comando inválido!\n")
        continue

    proxima_casa = labirinto[proxima_y][proxima_x]

    if proxima_casa == '#':
        print("Você não pode atravessar uma parede!\n")
    elif proxima_casa == 'S':
        print("Parabéns! Você encontrou a saída!\n")
        break
    elif proxima_casa == '-':
        labirinto[posicao_y][posicao_x] = '-'
        posicao_x = proxima_x
        posicao_y = proxima_y
        labirinto[posicao_y][posicao_x] = 'R'

print("Fim de jogo!")