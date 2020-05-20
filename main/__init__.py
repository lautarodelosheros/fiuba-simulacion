from gcl import GCL
from dado import Dado
import numpy
import matplotlib.pyplot as plt

gcl = GCL(97293, 1013904223, 1664525, 2**32)
dado = Dado(gcl)

suma = []
for _ in range(10000):
   suma.append(dado.lanzar() + dado.lanzar())

bins = numpy.arange(0, max(suma) + 1.5) - 0.5

fig, ax = plt.subplots()
_ = ax.hist(suma, bins)
ax.set_xticks(bins + 0.5)
plt.show()