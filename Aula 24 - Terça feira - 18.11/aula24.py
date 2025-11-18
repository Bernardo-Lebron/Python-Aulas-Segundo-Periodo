import matplotlib.pyplot as plt
import numpy as np

#exe01

a = np.array([1,2,3,4])
x = a.sum()
print(x)

b = np.array([[1,1], [2,2]])
y = b.sum(axis=0)
print(y)

#exe02

temperaturas = np.array([22.4, 23.1, 22.8, 23.0, 22.7, 22.9, 23.2, 22.7, 23.1, 23.6])

media = temperaturas.mean()
dp = temperaturas.std()
print(f"A média é: {media}")
print(f"O desvio padrão é: {dp}")
plt.boxplot(temperaturas)
plt.ylabel("Temperatura")
plt.grid(True)
plt.show()

#exe03

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

soma = A + B
print(soma)

#exe04

np.random.seed(42)

passos = np.random.choice([-1,1], size=100)
deslocamento = np.cumsum(passos)

plt.plot(deslocamento)
plt.title("Movimento Aleatório")
plt.xlabel("Passos")
plt.ylabel("Deslocamento")
plt.grid()
plt.show()