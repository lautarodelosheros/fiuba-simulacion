import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as m_lines
import matplotlib

from Gas import Gas

print()

PARTICLES = 1000
ROWS = 200
COLUMNS = 100
frame_num = 3000

gas = Gas(PARTICLES, ROWS, COLUMNS)
gas.map.remove_wall()


def get_color():
    return matplotlib.colors.to_hex(list(map(lambda x: x / 256, list(np.random.randint(256, size=3)))))


fig = plt.figure()
ax1 = plt.axes(xlim=(0, COLUMNS), ylim=(0, ROWS))
plt.xlabel('Longitude')
plt.ylabel('Latitude')

lines = []
for particle in gas.particles:
    lobj, = ax1.plot([], [], linewidth=0, color=particle.get_color(), marker='o', markersize="4")
    lines.append(lobj)


def init():
    for line in lines:
        line.set_data([], [])
    return lines


x1, y1 = [], []
x2, y2 = [], []

# wall = m_lines.Line2D([gas.map.wall_column, gas.map.wall_column], [0, ROWS], color='k')
# ax1.add_line(wall)


# fake data

iterations = []

for i in range(frame_num):
    x_list = []
    y_list = []


    for j in range(len(gas.particles)):
        x_list.append(gas.particles[j].column)
        y_list.append(gas.particles[j].row)

    iterations.append((x_list, y_list))
    gas.tick()

# print('len(gas.particles)', len(gas.particles))
# print('iterations[0][0][0]', iterations[0][0][0])


# print('iterations', len(iterations))


# print(lines)


def animate(i):
    # print('len(lines)', len(lines))
    # print('iteration', i)
    if i % 100 == 0:
        print('i', i)

    # lines = []

    for j in range(len(gas.particles)):
        # print('i', i)
        # print('j', j)
        # print('iterations[i]', iterations[i])
        # print('iterations[i][0', iterations[i][0])
        # print('iterations[i][1', iterations[i][1])
        lines[j].set_data(iterations[i][0][j], iterations[i][1][j])
    # iterations.append(lines)
    # gas.tick()

    return lines

    # return iterations[i]


def gen():
    i = 0
    while i < frame_num:
        yield i
        i += 1


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=gen, interval=1, blit=False, repeat=False)

plt.show()
