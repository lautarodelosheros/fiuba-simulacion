# GENERADOR CONGRUENCIAL LINEAL


class GCL:
    def __init__(self, x0, a, c, m):
        self.xn = x0
        self.a = a
        self.c = c
        self.m = m

    def random(self):
        self.xn = ((self.a * self.xn) + self.c) % self.m
        return self.xn

    def randomArray(self, n):
        numeros = []
        for _ in range(n):
            numeros.append(self.random())
        return numeros
