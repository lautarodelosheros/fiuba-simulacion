from typing import List

from Gas import Gas
from Map import Map
from Person import Person
from numpy import random
from math import ceil


class Society(Gas):
    def __init__(self, particles, rows, columns, sick_proportion=0.05):
        self.map = Map({"columns": columns, "rows": rows})
        self.map.remove_wall()

        rows_range = self.map.get_rows_range()
        columns_range = self.map.get_columns_range()

        self.particles: List[Person] = [
            Person(random.choice(rows_range), random.choice(columns_range), healthy=True, impact_radius=2,
                   disease_impat_probability=0.6, disease_cure_expected_days=20,
                   probability_of_curing=0.8) for x in range(particles)]

        sick_count = ceil(len(self.particles) * sick_proportion)

        print('sick count', sick_count)

        for i in range(sick_count):
            particle = random.choice(self.particles)
            particle.set_sick()

    def tick(self):
        for particle in self.particles:
            particle.move(self.map, self)
