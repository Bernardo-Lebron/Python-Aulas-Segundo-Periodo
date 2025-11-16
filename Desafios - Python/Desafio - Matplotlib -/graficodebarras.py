import matplotlib.pyplot as plt

#Grafico de barras

entrada = [100, 200, 300, 400, 500]

tempo_A = [0.5, 1.0, 1.5, 2.0, 2.5]
tempo_B = [0.6, 1.1, 1.8, 2.4, 3.0]

posicoes = [0, 1, 2, 3, 4]
largura = 0.35

posicao_A = [p - largura/2 for p in posicoes]
posicao_B = [p + largura/2 for p in posicoes]

plt.title("Tempo de execução de um algoritimo\nem função do tamanho da entrada")
plt.bar(posicao_A, tempo_A, width=largura, label="Computador A", color="red")
plt.bar(posicao_B, tempo_B, width=largura, label="Computador B", color="green")
plt.xticks(posicoes, entrada)
plt.xlabel("Tamanho da entrada")
plt.ylabel("Tempo de execução (seg)")
plt.legend()
plt.show()