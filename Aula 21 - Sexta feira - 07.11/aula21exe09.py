import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

plt.plot(names, values, color='red')
plt.bar(names, values)
plt.show()