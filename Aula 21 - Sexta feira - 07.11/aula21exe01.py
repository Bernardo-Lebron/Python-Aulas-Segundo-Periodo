import matplotlib.pyplot as plt


dados = [1, 4, 9, 13, 16, 25]

plt.plot(dados, linewidth=3)
plt.title("Dados", fontsize=24)
plt.xlabel("Obs", fontsize=14)
plt.ylabel("Valor", fontsize=14)
plt.tick_params(axis="both", labelsize=10)
plt.grid()
plt.show()