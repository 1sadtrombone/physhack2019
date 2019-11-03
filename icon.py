import numpy as np
import matplotlib.pyplot as plt

size = 0.5
n = 500

plt.ion()

l = 0.03
th  = np.linspace(0,2*np.pi)#2*np.pi * np.random.rand(n)
r = np.sin(th)
phi = 0#2*np.pi * np.random.rand(n)

while True:
    phi += 0.1

    bri = np.abs(np.sin((th-phi)*2.1)) / np.max(np.abs(np.sin((th-phi)*2.1)))
    
    plt.quiver(r*np.cos(th), r*np.sin(th), l*np.cos(phi), l*np.sin(phi), bri**3, angles='xy', scale_units='xy', scale=1, headlength=0, headwidth=1, pivot='mid', cmap='gray')
    ax = plt.gca()
    ax.set_facecolor('k')
    plt.pause(0.001)
    plt.clf()

