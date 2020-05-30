import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
from Gas import Gas

print()

gas = Gas()


# # Fixing random state for reproducibility
# np.random.seed(19680801)


def get_color():
    return matplotlib.colors.to_hex(list(map(lambda x: x / 256, list(np.random.randint(256, size=3)))))


fig = plt.figure()
ax1 = plt.axes(xlim=(0, 200), ylim=(0, 200))
line, = ax1.plot([], [], lw=0.1)
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# plotlays, plotcols = [2], ["black", "red"]
lines = []
for index in range(2):
    lobj, = ax1.plot([], [], linewidth=0, color=get_color(), marker='o')
    lines.append(lobj)


def init():
    for line in lines:
        line.set_data([], [])
    return lines


x1, y1 = [], []
x2, y2 = [], []

# fake data
frame_num = 24
gps_data = [-104 - (4 * np.random.rand(2, 3)), 31 + 3 * np.random.rand(2, 3)]


def animate(i):
    x = gas.particles[0].x
    y = gas.particles[0].y
    # print('x', x)
    # print('y', y)
    x1 = [x]
    y1 = [y]

    # print('x1', x1)
    # print('y1', y1)

    x2 = [x]
    y2 = [y]

    xlist = [x1, x2]
    ylist = [y1, y2]

    # for index in range(0,1):
    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])  # set data for each line separately.

    gas.tick()
    return lines


# animate(1)
# animate(2)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=10, blit=True)

plt.show()

# lines = []
# x1, y1 = [], []
# x2, y2 = [], []
#
#
# def init():
#     for line in lines:
#         line.set_data([], [])
#     return lines
#
#
# def update_lines(i):
#     x = [1, 2, 3]
#     y = [2, 3, 4]
#     x1.append(x)
#     y1.append(y)
#
#     x = [4, 5, 6]
#     y = [7, 8, 9]
#     x2.append(x)
#     y2.append(y)
#
#     xlist = [x1, x2]
#     ylist = [y1, y2]
#
#     for lnum, line in enumerate(lines):
#         # line.set_data(gas.particles[lnum].x, gas.particles[lnum].y)  # set data for each line separately.
#         line.set_data(xlist[lnum], ylist[lnum])
#
#     lines
#
#
# print()
#
# fig1 = plt.figure()
#
# for index in range(2):
#     lobj = plt.plot([], [], lw=2, color=get_color())[0]
#     lines.append(lobj)
#
# plt.xlim(0, 20)
# plt.ylim(0, 20)
# plt.xlabel('x')
# plt.title('test')
# line_ani = animation.FuncAnimation(fig1, update_lines, 25, init_func=init,
#                                    interval=1000, blit=True)
#
# x = np.arange(-9, 10)
# y = np.arange(-9, 10).reshape(-1, 1)
# base = np.hypot(x, y)
# ims = []
# # To save this second animation with some metadata, use the following command:
# # im_ani.save('im.mp4', metadata={'artist':'Guido'})
#
# plt.show()
