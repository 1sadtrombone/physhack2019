import numpy as np
import matplotlib.pyplot as plt

tmax = 1000
window = 100
n = 50
size = 100
pright = np.ones((size, size)) /2
phor = 0.5
pdown = np.ones((size, size)) /2
dx = np.zeros_like(pright)
dy = np.zeros_like(pright)

prevmax = 0

plt.ion()
for t in range(tmax):
    if t == 0:
        prev = np.zeros_like(pright)
        prev[prev.shape[0]//2,prev.shape[1]//2] = n
        print(np.sum(prev))
        cumul = np.array(prev)
    else:
        prev = dist.copy()
        cumul = np.dstack((cumul, prev))
        
    dist = np.zeros_like(prev)
    for x in range(dist.shape[0]):
        for y in range(dist.shape[1]):
        
            roll = np.random.rand(int(prev[x,y]))
            hor = np.sum(np.where(roll < phor, np.ones_like(roll), np.zeros_like(roll)))

            roll = np.random.rand(int(hor))
            right = np.sum(np.where(roll < pright[x,y], np.ones_like(roll), np.zeros_like(roll)))
            left = roll.shape[0] - right

            roll = np.random.rand(int(prev[x,y] - hor))
            down = np.sum(np.where(roll < pdown[x,y], np.ones_like(roll), np.zeros_like(roll)))
            up = roll.shape[0] - down
            
            dist[int(min(x+dx[x,y],dist.shape[0]-1)),y] += right
            dist[int(max(x-dx[x,y],0)),y] += left
            dist[x,int(min(y+dy[x,y],dist.shape[1]-1))] += up
            dist[x,int(max(y-dy[x,y],0))] += down


    dx = 3 * prev // np.max(prev)
    dy = 3 * prev // np.max(prev)

    dist[dist.shape[0]//2,dist.shape[1]//2] += n
    
    plt.imshow(dist, aspect='auto', cmap='plasma')
    plt.pause(0.001) 
    plt.clf()
    
plt.ioff()
plt.imshow(cumul, aspect='auto')
plt.show()
