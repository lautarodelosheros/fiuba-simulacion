import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as m_lines
import matplotlib

from Gas import Gas

print()

PARTICLES = 20000
ROWS = 200
COLUMNS = 100
frame_num = 3000

gas = Gas(PARTICLES, ROWS, COLUMNS)
LOWER_HALF_ONLY = True
gas.map.remove_wall(LOWER_HALF_ONLY)


def get_color():
    return matplotlib.colors.to_hex(list(map(lambda x: x / 256, list(np.random.randint(256, size=3)))))


fig = plt.figure()
ax1 = plt.axes(xlim=(0, COLUMNS), ylim=(0, ROWS))

# def init_density():


plt.xlabel('')
plt.ylabel('')

mat_g, = ax1.plot([], [], linewidth=0, color='g', marker='o', markersize="1")
mat_r, = ax1.plot([], [], linewidth=0, color='r', marker='o', markersize="1")
mats = [mat_g, mat_r]


def init():
    for mat in mats:
        mat.set_data([], [])
    return mats


wall = m_lines.Line2D([gas.map.wall_column, gas.map.wall_column], [0, ROWS // 2], color='k')
ax1.add_line(wall)

# fake data

iterations = []
left_densities = {"red": [], "green": []}
right_densities = {"red": [], "green": []}

for i in range(frame_num):
    x_list_g = []
    y_list_g = []
    x_list_r = []
    y_list_r = []

    if i % 100 == 0:
        print('iteration', i)

    for j in range(len(gas.particles)):
        particle = gas.particles[j]
        if particle.color == 'g':
            x_list_g.append(particle.column)
            y_list_g.append(particle.row)
        else:
            x_list_r.append(particle.column)
            y_list_r.append(particle.row)

    red_density_first_half, green_density_first_half, red_density_second_half, green_density_second_half = \
        gas.get_density_on_each_half()

    left_densities["red"].append(red_density_first_half)
    left_densities["green"].append(green_density_first_half)

    right_densities["red"].append(red_density_second_half)
    right_densities["green"].append(green_density_second_half)

    iterations.append(((x_list_g, y_list_g), (x_list_r, y_list_r)))
    gas.tick()

left_density_fig, left_density_ax = plt.subplots()
left_density_ax = plt.axes(xlim=(0, frame_num), ylim=(0, 1))

left_density_red_line, = left_density_ax.plot([], [], color='r')
left_density_green_line, = left_density_ax.plot([], [], color='g')
left_density_lines = [left_density_red_line, left_density_green_line]


def animate_left_density(i):
    if i % 100 == 0:
        print('animate left density', i)

    left_density_red_line.set_data(range(i), left_densities["red"][:i])
    left_density_green_line.set_data(range(i), left_densities["green"][:i])
    return left_density_lines


left_density_ani = animation.FuncAnimation(left_density_fig, animate_left_density, frames=frame_num,
                                           interval=25, blit=True, repeat=False)

right_density_fig, right_density_ax = plt.subplots()
right_density_ax = plt.axes(xlim=(0, frame_num), ylim=(0, 1))

right_density_red_line, = right_density_ax.plot([], [], color='r')
right_density_green_line, = right_density_ax.plot([], [], color='g')
right_density_lines = [right_density_red_line, right_density_green_line]


def animate_right_density(i):
    if i % 100 == 0:
        print('animate right density', i)

    right_density_red_line.set_data(range(i), right_densities["red"][:i])
    right_density_green_line.set_data(range(i), right_densities["green"][:i])
    return right_density_lines


right_density_ani = animation.FuncAnimation(right_density_fig, animate_right_density, frames=frame_num,
                                            interval=25, blit=True, repeat=False)


def animate(i):
    if i % 100 == 0:
        print('animate', i)

    mats[0].set_data(iterations[i][0][0], iterations[i][0][1])
    mats[1].set_data(iterations[i][1][0], iterations[i][1][1])

    return mats


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=50, blit=True, repeat=False)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

prefix = str(PARTICLES) + '-' + str(frame_num) + '_lower_half' if LOWER_HALF_ONLY else ''
anim.save(prefix + '_common_output.mp4')

# Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

left_density_ani.save(prefix + '_left_density_output.mp4')
right_density_ani.save(prefix + '_right_density_output.mp4')

# plt.show()
