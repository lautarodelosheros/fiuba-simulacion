from typing import List

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.lines as m_lines
from matplotlib.lines import Line2D
from MovementType import MovementType
import matplotlib

from Society import Society

print()

PARTICLES = 100
ROWS = 100
COLUMNS = 100
days = 300


def render_model(model_properties):
    society = Society(PARTICLES, ROWS, COLUMNS, movement_type=model_properties["movement"],
                      cure=model_properties["cure"], sick_proportion=0.05)

    fig = plt.figure()
    ax1 = plt.axes(xlim=(0, COLUMNS), ylim=(0, ROWS))

    healthy_fig, healthy_ax = plt.subplots()
    healthy_ax = plt.axes(xlim=(0, days), ylim=(0, PARTICLES))

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

    iterations = []
    healthy_iterations = []
    sick_iterations = []

    for i in range(days):
        x_list = []
        y_list = []
        color_list = []

        for j in range(len(society.particles)):
            x_list.append(society.particles[j].column)
            y_list.append(society.particles[j].row)
            color_list.append(society.particles[j].get_color())

        healthy_iterations.append(society.get_healthy_count())
        sick_iterations.append(PARTICLES - society.get_healthy_count())
        iterations.append((x_list, y_list, color_list))
        society.tick()

    healthy_line, = healthy_ax.plot([], [], color='g')
    sick_line, = healthy_ax.plot([], [], color='r')
    healthy_lines = [healthy_line, sick_line]

    def animate_healthy(i):
        healthy_line.set_data(range(i), healthy_iterations[:i])
        sick_line.set_data(range(i), sick_iterations[:i])
        return healthy_lines

    def animate(i):
        for j in range(len(society.particles)):
            lines[j].set_data(iterations[i][0][j], iterations[i][1][j])
            if i > 0 and iterations[i][2][j] != iterations[i - 1][2][j]:
                lines[j].set_color(iterations[i][2][j])

        return lines

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=days, interval=100, blit=True, repeat=False)

    health_anim = animation.FuncAnimation(healthy_fig, animate_healthy,
                                          frames=days, interval=100, blit=True, repeat=False)

    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)

    anim.save('output ' + model_properties["name"] + '.mp4')
    health_anim.save('output ' + model_properties["name"] + '_healthy_graph.mp4')

    # plt.show()


models = [
    {"name": "a-free-movement", "movement": MovementType.FREE, "cure": True},
    {"name": "a-quarantine", "movement": MovementType.QUARANTINE, "cure": True},
    {"name": "a-half", "movement": MovementType.HALF, "cure": True},
    {"name": "b-free-movement", "movement": MovementType.FREE, "cure": False},
    {"name": "b-quarantine", "movement": MovementType.QUARANTINE, "cure": False},
    {"name": "b-half", "movement": MovementType.HALF, "cure": False}
]

for model in models:
    render_model(model)
