import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import scipy.interpolate as scip

#exe01

def f(x):
    return x**2

resultado, erro = spi.quad(f, 0, 2)

print(resultado)
print(erro)

#exe02

def f(x, y):
    return x**2 + y **2

resultado, erro = spi.dblquad(f, 0, 1, 0, 2)
print(f"Resultado da integral dupla: {resultado}")
print(f"Erro estimado: {erro}")

#exe03

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

f_linear = scip.interp1d(x, y, kind='linear')
y_1 = f_linear(x)

plt.plot(x, y, label='Dados originais') 
plt.plot(x, y_1, label='Interpolação Linear')
plt.legend()
plt.title('Interpolação Linear')
plt.show()

#exe04

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])
polinomio = scip.lagrange(x, y)
print(polinomio)
y_new = polinomio(x)

plt.plot(x, y, 'o', label='Pontos conhecidos') # Pontos conhecidos
plt.plot(x, y_new, '-', label='Polinômio de Lagrange') # Polinômio
plt.legend()
plt.title('Interpolação de Lagrange')
plt.show()