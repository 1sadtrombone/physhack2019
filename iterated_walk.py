import numpy as np
import matplotlib.pyplot as plt

iters = 5
n = 50
steps = 1001
pright = np.zeros(100)
dist = np.zeros_like(pright)

for it in range(iters):
    fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)    
    ax1.plot(pright, 'r')
    for particle in range(n):
        pos = np.shape(dist)[0] // 2
        path = [pos]
        for i in range(steps):
            roll = np.random.randint(0, 100+1) / 100
            if roll > pright[pos]:
                pos -= 1
            else:
                pos += 1
            path.append(pos)
    
        dist[pos] += 1

        #plt.plot(path)
        #plt.show()
        #plt.clf()

        pright = dist * 100 / max(dist)
        
    ax0.plot(dist, 'k')
    plt.show()
