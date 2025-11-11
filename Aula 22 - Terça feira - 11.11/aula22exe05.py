import matplotlib.pyplot as plt

tempos = [12, 14, 11, 15, 13, 16, 14, 15, 10, 17]

plt.boxplot(tempos, patch_artist=False)
plt.show()