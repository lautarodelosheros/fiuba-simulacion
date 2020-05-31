from typing import List

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as m_lines
from matplotlib.lines import Line2D
import matplotlib

from Society import Society

print()

PARTICLES = 100
ROWS = 100
COLUMNS = 100
days = 300

society = Society(PARTICLES, ROWS, COLUMNS)

fig = plt.figure()
ax1 = plt.axes(xlim=(0, COLUMNS), ylim=(0, ROWS))
plt.xlabel('Longitude')
plt.ylabel('Latitude')

lines: List[Line2D] = []
for particle in society.particles:
    lobj, = ax1.plot([], [], linewidth=0, color=particle.get_color(), marker='o', markersize="4")
    lines.append(lobj)


def init():
    for line in lines:
        line.set_data([], [])
    return lines


x1, y1 = [], []
x2, y2 = [], []

iterations = []

for i in range(days):
    x_list = []
    y_list = []
    color_list = []

    for j in range(len(society.particles)):
        x_list.append(society.particles[j].column)
        y_list.append(society.particles[j].row)
        color_list.append(society.particles[j].get_color())

    iterations.append((x_list, y_list, color_list))
    society.tick()


def animate(i):
    # if i % 100 == 0:
    #     print('i', i)
    print('i', i)

    # lines = []

    for j in range(len(society.particles)):
        lines[j].set_data(iterations[i][0][j], iterations[i][1][j])
        if i > 0 and iterations[i][2][j] != iterations[i - 1][2][j]:
            lines[j].set_color(iterations[i][2][j])

    return lines


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=days, interval=10, blit=True, repeat=False)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

anim.save('output.mp4')


# plt.show()