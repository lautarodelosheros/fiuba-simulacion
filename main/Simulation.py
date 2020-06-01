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

mat_g, = ax1.plot([], [], linewidth=0, color='g', marker='o', markersize="1")
mat_r, = ax1.plot([], [], linewidth=0, color='r', marker='o', markersize="1")
mats = [mat_g, mat_r]

def init():
    for mat in mats:
        mat.set_data([], [])
    return mats

# wall = m_lines.Line2D([gas.map.wall_column, gas.map.wall_column], [0, ROWS], color='k')
# ax1.add_line(wall)


# fake data

iterations = []

for i in range(frame_num):
    x_list_g = []
    y_list_g = []
    x_list_r = []
    y_list_r = []

    for j in range(len(gas.particles)):
        particle = gas.particles[j]
        if particle.color == 'g':
            x_list_g.append(particle.x)
            y_list_g.append(gas.particles[j].y)
        else:
            x_list_r.append(particle.x)
            y_list_r.append(gas.particles[j].y)

    iterations.append(((x_list_g, y_list_g), (x_list_r, y_list_r)))
    gas.tick()


# print('len(gas.particles)', len(gas.particles))
# print('iterations[0][0][0]', iterations[0][0][0])


# print('iterations', len(iterations))


# print(lines)


def animate(i):

    mats[0].set_data(iterations[i][0][0], iterations[i][0][1])
    mats[1].set_data(iterations[i][1][0], iterations[i][1][1])

    return mats


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=1, blit=True, repeat=False)

# Set up formatting for the movie files
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

#anim.save('output.mp4')

plt.show()