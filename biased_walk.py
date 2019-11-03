import numpy as np
import matplotlib.pyplot as plt

n = 500
steps = 1001
pright = np.linspace(200, 0, 100)
dist = np.zeros(100)

for particle in range(n):
    pos = 0
    path = [0]
    for i in range(steps):
        roll = np.random.randint(0, 100+1)
        
        if roll > pright[pos]:
            pos -= 1
        else:
            pos += 1
        path.append(pos)

    dist[pos] += 1
#    plt.plot(path)
#    plt.show()
#    plt.clf()

plt.plot(dist, 'k')
plt.show()
