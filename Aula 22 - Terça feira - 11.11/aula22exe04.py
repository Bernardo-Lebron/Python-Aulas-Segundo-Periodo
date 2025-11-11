import matplotlib.pyplot as plt

alturas = [160, 165, 170, 175, 180, 185]
pesos = [55, 60, 65, 70, 75, 80]

plt.scatter(alturas, pesos, color='red')
plt.title("Altura x Peso")
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.show()