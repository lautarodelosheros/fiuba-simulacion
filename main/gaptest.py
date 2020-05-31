from gcl import GCL
from scipy.stats import chi2

MIN = 0.2
MAX = 0.5
N = 100000

def gaptestGCL(minimo, maximo, n):
    gcl = GCL(97293, 1013904223, 1664525, 2**32)
    while not (minimo < gcl.random() < maximo):
        continue
    gaps = [0] * 26
    for _ in range(n):
        gap = 0
        while not (minimo < gcl.random() < maximo): gap += 1
        if gap >= 25: gaps[-1] += 1
        else: gaps[gap] += 1
    return gaps

def expected(i):
    if i == 25:
        return ((1 - (MAX - MIN)) ** 25) * N
    return ((1 - (MAX - MIN)) ** i) * (MAX - MIN) * N

def create_D2(observed, f_expected):
    D2 = []
    for i in range(len(observed)):
        expected = f_expected(i)
        D2.append((observed[i] - expected) ** 2 / expected)
    return D2

def testchi2(sig, df, D2):
    total = sum(D2)
    limite_superior = chi2.ppf(1 - sig, df)
    print('D2 = {}'.format(total))
    print('limite superior = {}'.format(limite_superior))
    if total <= limite_superior:
        print("No hay evidencia para rechazar la hipótesis nula, el generador pasa el test.")
    else:
        print("Hay evidencia para rechazar la hipótesis nula, el generador no pasa el test.")

def main():
    muestra_gaps = gaptestGCL(MIN, MAX, N)
    D2 = create_D2(muestra_gaps, expected)
    testchi2(10e-2, 25, D2)

main()