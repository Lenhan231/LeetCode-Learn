import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import pi, sqrt

fig, ax = plt.subplots()
x = np.linspace(-sqrt(pi), sqrt(pi), 1000)
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 3)
line, = ax.plot([], [], 'r-')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    y = np.sin(x + 2 * pi * frame / 100)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=10, init_func=init, blit=True)
plt.show()
