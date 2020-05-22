import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
import scipy.integrate
from gcl import GCL


def f(x):
    return (13 / (12 * np.pi)) - (1 / np.pi ** 3) * x ** 2


def F(x):
    return (scipy.integrate.quad(f, -np.pi / 2, x))[0]
    #return (-x ** 3 / (3 * np.pi ** 3)) + (13 / 12 * np.pi) * x + 0.5

def main():
    x = np.linspace(-np.pi / 2, np.pi / 2, 100)
    y = [0] * 100
    for i in range(100):
        y[i] = F(x[i])
    Finv = scipy.interpolate.interp1d(y, x)
    gcl = GCL(97293, 1013904223, 1664525, 2 ** 32)

    u = gcl.randomArray(100000)
    v = Finv(u)

    plt.hist(v, bins=10)
    plt.show()


def graficar(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')
    plt.show()
