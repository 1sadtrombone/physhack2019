import numpy as np
import matplotlib.pyplot as plt

iters = 1
n = 50 # no of particles
steps = 1000 # no of steps

size = 100

pright = np.ones(size) / 2
dist = np.zeros_like(pright)

for i in range(iters):

    rolls = np.random.rand(n, steps)
    dx = np.where(rolls > pright, np.ones((n, steps)), -np.ones((n, steps)))
    x = np.cumsum(dx, axis=1)
    plt.plot(x)
