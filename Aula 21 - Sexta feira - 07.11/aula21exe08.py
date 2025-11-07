import matplotlib.pyplot as plt

cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

plt.plot(activity, dog, label="dog")
plt.plot(activity, cat, label="cat")
plt.legend()
plt.show()