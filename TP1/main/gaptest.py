from gcl import GCL
from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy 

MIN = 0.2
MAX = 0.5
N = 100000

def gaptestGCL(minimo, maximo, n):
    gcl = GCL(97293, 1013904223, 1664525, 2**32)
    while not (minimo < gcl.random() < maximo):
        continue
    gaps_dict = {}
    for _ in range(n):
        gap = 0
        while not (minimo < gcl.random() < maximo): 
            gap += 1
        gaps_dict[gap] = gaps_dict.get(gap, 0) + 1
    gaps = [0] * (max(gaps_dict.keys())  + 1)

    gap = [0] * n
    index = 0
    longitud = 0
    gcl = GCL(97293, 1013904223, 1664525, 2**32)
    while index < n:
        if minimo < gcl.random() < maximo:
            gap[index] = longitud
            index += 1
            longitud = 0
        else:
            longitud += 1
    bins = numpy.arange(0, max(gap) + 1.5) - 0.5

    for g in gaps_dict:
        gaps[g] = gaps_dict[g]
    muestra_bins = [gaps[i] if i < 25 else sum(gaps[i:]) for i in range(26)]
    return gaps, muestra_bins, bins, gap

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

def graficar_hist(muestra, bins):

    # bins = numpy.arange(0, max(muestra) + 1.5) - 0.5

    fig, ax = plt.subplots()

    (hist, _, _) = ax.hist(muestra, bins)
    ax.set_xticks(bins + 0.5)
    plt.show()


    # fig, ax = plt.subplots()
    # ax.hist(muestra, bins=len(muestra))
    # plt.show()


def old():
    a = 0.2
    b = 0.5

    gcl = GCL(97293, 1013904223, 1664525, 2**32)

    numero_gaps = 100000
    gap = [0] * numero_gaps

    while not (a < gcl.random() < b):
        continue

    n = 0
    longitud = 0
    while n < numero_gaps:
        if a < gcl.random() < b:
            gap[n] = longitud
            n += 1
            longitud = 0
        else:
            longitud += 1
        
    bins = numpy.arange(0, max(gap) + 1.5) - 0.5

    # print('gap', gap)
    print('gap', gap)


def main():
    muestra_gaps, muestra_bins, bins, gap = gaptestGCL(MIN, MAX, N)
    D2 = create_D2(muestra_bins, expected)
    testchi2(10e-2, 25, D2)
    graficar_hist(gap, bins)

main()
