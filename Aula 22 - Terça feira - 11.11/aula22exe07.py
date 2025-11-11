import matplotlib.pyplot as plt

dias = ["Domingo","Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
temperatura = [22, 24, 23, 25, 21, 20, 22]

plt.plot(dias, temperatura, marker='o', color='red', linestyle='--')
plt.title("Temperatura durante a semana")
plt.xlabel("Dia")
plt.ylabel("Temperatura")
plt.show()