import matplotlib.pyplot as plt

plt.title("Quadrados", fontsize=24)

xdata = [1, 2, 3, 4, 5]
ydata = [1, 4, 9, 16, 25]

plt.axis([0, 6, 0, 30])
plt.scatter(xdata, ydata, c='red', edgecolor='none', s=40)
plt.show()

