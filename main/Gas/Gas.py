from typing import List

from Map import Map
from Particle import Particle
import random


class Gas:
    def __init__(self, particles, rows, columns):
        self.map = Map({"columns": columns, "rows": rows})
        half_particles = particles // 2

        first_half_range = self.map.get_half_columns_range(True)
        second_half_range = self.map.get_half_columns_range(False)
        rows_range = self.map.get_rows_range()

        first_half = [Particle(random.choice(rows_range), random.choice(first_half_range)) for x in
                      range(half_particles)]
        second_half = [Particle(random.choice(rows_range), random.choice(second_half_range), False) for x in
                       range(half_particles + (1 if particles % 2 > 0 else 0))]

        self.particles: List[Particle] = first_half + second_half

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
