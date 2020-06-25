# SIMULACION DADO DE N CARAS
import math


class Dado:
    def __init__(self, generador, caras = 6):
        self.caras = caras
        self.generador = generador

    def lanzar(self):
        return math.ceil(self.generador.random() * self.caras)

    def lanzarTantoComo(self, n):
        lanzamientos = []
        for _ in range(n):
            lanzamientos.append(self.lanzar())
        return lanzamientos
