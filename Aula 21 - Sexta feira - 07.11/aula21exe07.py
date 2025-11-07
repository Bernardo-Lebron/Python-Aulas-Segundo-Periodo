import matplotlib.pyplot as plt

fruit_weights = [(1,2,3,4,3,2,3,4,5,3,2,1,2,3,4,5),(2,3,4,5,6,4,3,4,5,3,6,7,8,9,4,10,2,)]

labels = ['peaches', 'oranges']

plt.boxplot(fruit_weights, tick_labels=labels)
plt.show()