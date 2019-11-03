import numpy as np
import matplotlib.pyplot as plt

tmax = 1000
tstart = 0
window = 100
n = 1000
size = 100
pright = np.ones(size) /2
dx = np.zeros_like(pright)

prevmax = 0

plt.ion()
for t in range(tmax):
    if t == 0:
        prev = np.zeros_like(pright)
        prev[prev.shape[0]//2] = n
        cumul = np.array([prev])
    else:
        prev = dist.copy()
        cumul = np.vstack((cumul, prev))
    dist = np.zeros_like(prev)

    for pos in range(dist.shape[0]):
        
        roll = np.random.rand(int(prev[pos]))
        right = np.sum(np.where(roll < pright[pos], np.ones_like(roll), np.zeros_like(roll)))
        left = roll.shape[0] - right

        dist[int(min(pos+dx[pos],dist.shape[0]-1))] += right
        
        dist[int(max(pos-dx[pos],0))] += left
    #plt.plot(dist, 'k')
    #plt.plot(pright, 'r')
    if t > tstart:
        extent = (0, size, t, max(0, t-window))
        plt.imshow(cumul[max(0,t-window):t], extent=extent, aspect='auto')
        plt.pause(0.001) 
        plt.clf()
    dx = 3 * prev // np.max(prev)
    
plt.ioff()
plt.imshow(cumul, aspect='auto')
plt.show()
