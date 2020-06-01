from typing import List

from Gas import Gas
from Map import Map
from Person import Person
from numpy import random
from math import ceil
from MovementType import MovementType


class Society(Gas):
    def __init__(self, particles: int, rows: int, columns: int, sick_proportion: float = 0.05,
                 movement_type=MovementType.FREE, cure=True):
        self.map = Map(columns, rows)
        self.map.remove_wall()

        if movement_type != MovementType.HALF:
            self.particles: List[Person] = [
                Person(random.randint(1, rows), random.randint(1, columns), healthy=True, impact_radius=2,
                       disease_impat_probability=0.6, disease_cure_expected_days=20,
                       probability_of_curing=0.8, movement_type=movement_type, cure=cure) for x in range(particles)]
        else:
            print('movement is half')
            self.particles: List[Person] = [
                                               Person(random.randint(1, rows), random.randint(1, columns), healthy=True,
                                                      impact_radius=2,
                                                      disease_impat_probability=0.6, disease_cure_expected_days=20,
                                                      probability_of_curing=0.8, movement_type=MovementType.FREE,
                                                      cure=cure) for x
                                               in range(particles // 2)
                                           ] + [
                                               Person(random.randint(1, rows), random.randint(1, columns), healthy=True,
                                                      impact_radius=2,
                                                      disease_impat_probability=0.6, disease_cure_expected_days=20,
                                                      probability_of_curing=0.8, movement_type=MovementType.STILL,
                                                      cure=cure) for x
                                               in range(particles // 2)
                                           ]

        sick_count = ceil(len(self.particles) * sick_proportion)

        print('sick count', sick_count)

        for i in range(sick_count):
            particle = random.choice(self.particles)
            particle.set_sick()

    def tick(self):
        for particle in self.particles:
            particle.move(self.map, self)
