import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr"]
Parque_A = [200, 220, 250, 270]
Parque_B = [180, 210, 240, 260]

posicoes = [0, 1, 2, 3]
largura = 0.35

posicao_A = [p - largura/2 for p in posicoes]
posicao_B = [p + largura/2 for p in posicoes]

plt.bar(posicao_A, Parque_A, label="Parque_A")
plt.bar(posicao_B, Parque_B, label="Parque_B")
plt.xticks(posicoes, meses)
plt.title("Visitantes por Parque")
plt.xlabel("Mês")
plt.ylabel("Número de visitantes")
plt.legend()
plt.show()