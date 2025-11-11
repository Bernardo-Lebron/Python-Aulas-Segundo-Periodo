import matplotlib.pyplot as plt

semanas = [1, 2, 3, 4, 5]
planta_a = [2, 4, 6, 7, 10]
planta_b = [1, 3, 5, 7, 9]

plt.plot(semanas, planta_a, marker='o', color='red', label='planta_a')
plt.plot(semanas, planta_b, marker='s', color='green', label='planta_b')
plt.title("Crescimento de Plantas")
plt.xlabel("Semana")
plt.ylabel("Altura(cm)")
plt.legend()
plt.show()
