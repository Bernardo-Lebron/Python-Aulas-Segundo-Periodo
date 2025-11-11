import matplotlib.pyplot as plt

frutas = "Maçã", "Banana", "Laranja", "Uva"
Porcentagem = [40, 30, 20, 10]

explode = [0, 0.1, 0, 0]

plt.pie(Porcentagem, labels=frutas, autopct='%1.1f%%', explode=explode)
plt.show()