import numpy as np
import matplotlib.pyplot as plt


def softmax(x_ls, beta=1):
    exp_x = np.exp(beta * x_ls)
    return exp_x / exp_x.sum(axis=0, keepdims=True)


x = np.random.rand(500) * 10 - 5
y = softmax(x, beta=5)

plt.scatter(x, y)
plt.show()
