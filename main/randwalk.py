import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = 0
y = 0

fig, ax = plt.subplots()
ax.set_xlim(-25, 25)
ax.set_ylim(-20, 20)
mat, = ax.plot(x, y, 'o')

def animate_rw(i):

    global x
    global y
    siguiente = random.randint(1, 4)

    if siguiente < 3:
        if siguiente == 1:
            x += 1
        else:
            x -= 1
    elif siguiente == 3:
        y += 1
    else:
        y -= 1

    mat.set_data([x], [y])
    return mat,

def gen():
    i = 0
    while i < 1000:
        yield i
        i += 1

anim = FuncAnimation(fig, animate_rw, interval=100, blit=True, frames=gen, repeat=False)
plt.show()