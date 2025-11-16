import matplotlib.pyplot as plt

#Grafico de linhas

entrada = [100, 200, 300, 400, 500]

tempo_A = [0.5, 1.0, 1.5, 2.0, 2.5]
tempo_B = [0.6, 1.1, 1.8, 2.4, 3.0]

plt.title("Tempo de execução de um algoritimo\nem função do tamanho da entrada")
plt.plot(entrada, tempo_A, label="Computador A", color="red", marker='o')
plt.plot(entrada, tempo_B, label="Computador B", color="green",  marker='o')
plt.xlabel("Tamanho da entrada")
plt.ylabel("Tempo de execução (seg)")
plt.legend()
plt.show()