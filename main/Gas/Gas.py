from Map import Map
from Particle import Particle
import random


class Gas:
    def __init__(self, particles, rows, columns):
        self.map = Map(columns, rows)

        first_half = [Particle(random.randint(1, columns // 2), random.randint(1, rows), 'g') for x in
                      range(particles // 2)]
        second_half = [Particle(random.randint(columns // 2 + 1, columns), random.randint(1, rows), 'r') for x in
                       range(particles // 2 + (1 if particles % 2 == 0 else 0))]

        self.particles = first_half + second_half

    def tick(self):
        for particle in self.particles:
            particle.move(self.map)

    def __str__(self):
        return ", ".join(
            map(lambda particle: str(particle), self.particles))


if __name__ == '__main__':
    print()
    gas = Gas()
    print(gas)
    gas.tick()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
    # gas = Gas()
