import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def modelo(t, A, k, C):
    return A * np.exp(-k * t) + C

np.random.seed(0)  

t = np.linspace(0, 10, 50)  

A = 5
k = 0.8
C = 1

ruido = np.random.normal(0, 0.5, size=len(t))
y = modelo(t, A, k, C) + ruido

chute_inicial = [4, 1, 0]

param_est, _ = curve_fit(modelo, t, y, p0=chute_inicial)

A_est, k_est, C_est = param_est

erro_A = abs(A_est - A)
erro_k = abs(k_est - k)
erro_C = abs(C_est - C)

print("Parâmetros estimados:")
print(f"A = {A_est} (erro = {erro_A})")
print(f"k = {k_est} (erro = {erro_k})")
print(f"C = {C_est} (erro = {erro_C})")

plt.figure(figsize=(9, 5))
plt.scatter(t, y, label="Dados experimentais (com ruído)", marker='o')
plt.plot(t, modelo(t, A_est, k_est, C_est), label="Curva ajustada", linewidth=2)
plt.xlabel("t (s)")
plt.ylabel("y(t)")
plt.title("Ajuste de Curva Exponencial")
plt.legend()
plt.grid(True)
plt.show()
