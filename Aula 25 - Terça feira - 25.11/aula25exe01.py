import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

hora = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = [42, 53, 61, 72, 79, 83, 90, 102, 111, 119]

def modelo_linear(x, a, b):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return a * x + b

params, cov = curve_fit(modelo_linear, hora, temp)
a, b = params

print(f"Coeficiente angular (a): {a:.4f}")
print(f"Intercepto (b): {b:.4f}")

temp_ajustada = modelo_linear(hora, a, b)

plt.figure(figsize=(10, 5))
plt.scatter(hora, temp, label="Dados originais")
plt.plot(hora, temp_ajustada, label="Modelo linear ajustado")
plt.xlabel(("Tempo (h)"))
plt.ylabel("Temperatura (C)")
plt.title("Ajuste Linear da Temperaturaa em Função do Tempo")
plt.grid(True)
plt.legend()
plt.show()