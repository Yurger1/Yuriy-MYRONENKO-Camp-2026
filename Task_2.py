import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size = 20
grid = np.random.choice([0, 1], (size, size), p=[0.7, 0.3])

def update(frame):
    global grid
    total = sum(np.roll(np.roll(grid, i, 0), j, 1)
                for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))
    
    grid = ((grid == 1) & ((total == 2) | (total == 3))) | ((grid == 0) & (total == 3))
    img.set_data(grid)
    return img,

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='Greens')

ani = FuncAnimation(fig, update, frames=50, interval=200)
plt.show()