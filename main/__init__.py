from gcl import GCL
from dado import Dado
import matplotlib.pyplot as plt

gcl = GCL(97293, 1013904223, 1664525, 232)
dado = Dado(gcl)

suma = []
for _ in range(10000):
    suma.append(dado.lanzar() + dado.lanzar())

plt.hist(suma, bins=12, range=[2, 12])
plt.show()