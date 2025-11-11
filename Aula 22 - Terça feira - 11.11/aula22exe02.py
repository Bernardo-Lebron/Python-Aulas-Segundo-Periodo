import matplotlib.pyplot as plt

estudantes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
livros = [5, 7, 3, 8, 6]

plt.bar(estudantes, livros)
plt.xlabel("Estuantes")
plt.ylabel("Qtd de Livros")
plt.show()