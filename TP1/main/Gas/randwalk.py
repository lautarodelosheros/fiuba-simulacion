import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from Gas import Particle
from Gas import Map

x = 0
y = 0
x_data = []
y_data = []

fig = plt.figure()
ax1 = plt.axes(xlim=(0, 50), ylim=(0, 50))
mat, = ax1.plot([], [], linewidth=0, color='b', marker='o', markersize="4")
line, = ax1.plot(0, 0, color='b', lw=1.1, ls='dashed', markersize="0")

frames = 1000

particle = Particle(25, 25, 'b')
available_map = Map(50, 50)


def animate_rw(i):
    column = particle.column
    row = particle.row

    x_data.append(column)
    y_data.append(row)
    mat.set_data([column], [row])
    line.set_xdata(x_data)
    line.set_ydata(y_data)

    particle.move(available_map)

    return mat, line,


anim = animation.FuncAnimation(fig, animate_rw, interval=100, blit=True, frames=frames, repeat=False)
# plt.show()

Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

anim.save('ej-8.mp4')
