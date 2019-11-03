import numpy as np
import matplotlib.pyplot as plt

size = 0.5
n = 500

plt.ion()

r = size * np.random.rand(n)
l = 0.03
th  = 2*np.pi * np.random.rand(n)
phi = 2*np.pi * np.random.rand(n)

rotspeed = 0.03 + 0.01 * (np.random.rand(n) - 0.5)

while True:
    phi += rotspeed
    bri = np.abs(np.sin((th-phi))) / np.max(np.abs(np.sin((th-phi))))

    plt.quiver(r*np.cos(th), r*np.sin(th), l*np.cos(phi), l*np.sin(phi), bri**3, angles='xy', scale_units='xy', scale=1, headlength=0, headwidth=1, pivot='mid')
    ax = plt.gca()
    ax.set_facecolor('k')
    plt.pause(0.001)
    plt.clf()

