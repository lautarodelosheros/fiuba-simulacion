from typing import List

from Particle import Particle
from math import sqrt
from math import pow
from numpy import random


class Person(Particle):
    def __init__(self, x, y, first_half=True, healthy=True, impact_radius=2, disease_impat_probability=0.6,
                 disease_cure_expected_days=20, probability_of_curing=0.8, mode_randomly=False, quarantine=False):
        super(Person, self).__init__(x, y, first_half)

        self.healthy = healthy
        self.impact_radius = impact_radius
        self.disease_impact_probability = disease_impat_probability
        self.disease_cure_expected_days = disease_cure_expected_days
        self.probability_of_curing = probability_of_curing

        self.color = self.get_color()

        self.sick_days = 0

    def get_color(self):
        return 'g' if self.healthy else 'r'

    def move(self, available_map, society):
        super(Person, self).move(available_map)

        if not self.healthy:
            self.sick_days += 1
            self.spread_disease(society)

        if self.sick_days >= self.disease_cure_expected_days:
            random_number = random.uniform(0, 1)
            if random_number < self.probability_of_curing:
                print('I HEALED')
                self.healthy = True
                self.sick_days = 0

    def spread_disease(self, society):
        if self.healthy:
            return

        people = society.particles

        neighbours: List[Person] = filter(lambda other_person: is_neighbour(self, other_person, self.impact_radius),
                                          people)

        # if len(neighbours) > 0:
        #     print('found neighbours', len(neighbours))

        for neighbour in neighbours:
            neighbour.get_disease()

    def get_disease(self):
        if not self.healthy:
            return

        random_number = random.uniform(0, 1)
        if random_number < self.disease_impact_probability:
            self.healthy = False

    def set_sick(self):
        self.healthy = False


def is_neighbour(root: Person, other: Person, distance: int):
    if root == other:
        return False

    return sqrt(pow(root.row - other.row, 2) + pow(root.column - other.column, 2)) < distance
