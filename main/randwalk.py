import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = 0
y = 0
x_data = []
y_data = []
fig, ax = plt.subplots()
ax.axis([-25, 25, -20, 20])
line, = ax.plot(0, 0, color='b', lw=1.1, ls='dashed')
mat, = ax.plot(x, y, 'o', color='b')

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

    x_data.append(x)
    y_data.append(y)
    mat.set_data([x], [y])
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return mat, line,

def gen():
    i = 0
    while i < 1000:
        yield i
        i += 1

anim = FuncAnimation(fig, animate_rw, interval=100, blit=True, frames=gen, repeat=False)
plt.show()
