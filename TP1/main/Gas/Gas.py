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

    def get_density_on_each_half(self):
        first_half = [particle for particle in self.particles if particle.column <= self.map.wall_column]
        second_half = [particle for particle in self.particles if particle.column > self.map.wall_column]

        first_half_red = [particle for particle in first_half if particle.get_color() == 'r']
        second_half_red = [particle for particle in second_half if particle.get_color() == 'r']

        red_density_first_half = len(first_half_red) / len(first_half)
        green_density_first_half = (len(first_half) - len(first_half_red)) / len(first_half)
        red_density_second_half = len(second_half_red) / len(second_half)
        green_density_second_half = (len(second_half) - len(second_half_red)) / len(second_half)

        return red_density_first_half, green_density_first_half, red_density_second_half, green_density_second_half

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
