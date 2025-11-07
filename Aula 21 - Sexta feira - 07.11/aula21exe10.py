import matplotlib.pyplot as plt

# Gráfico 1
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Gráfico 1')

# Gráfico 2
plt.subplot(2, 2, 2)
plt.bar([1, 2, 3], [3, 5, 7])
plt.title('Gráfico 2')

# Gráfico 3
plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3], [9, 4, 1])
plt.title('Gráfico 3')

# Gráfico 4
plt.subplot(2, 2, 4)
plt.hist([1, 1, 2, 3, 3, 3, 4, 5])
plt.title('Gráfico 4')

# Ajustar o layout
plt.tight_layout()
plt.suptitle("Nome da Figura",fontsize=20)
plt.show()