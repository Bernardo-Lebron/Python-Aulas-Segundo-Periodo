import matplotlib.pyplot as plt

x = list(range(1,11))
y = [i*2 for i in x]

plt.plot(x, y, marker='o', color='blue')
plt.xlabel("Numero")
plt.ylabel(("Numero * 2"))
plt.show()