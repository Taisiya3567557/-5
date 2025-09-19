import random
import numpy as np
from bird import Bird
from config import *

class Population:
    def __init__(self, size=POPULATION_SIZE):
        self.birds = [Bird() for _ in range(size)]
        self.generation = 1

    def all_dead(self):
        return all(not bird.alive for bird in self.birds)

    def calculate_fitness(self):
        total = sum(bird.score for bird in self.birds)
        for bird in self.birds:
            bird.fitness = bird.score / total if total > 0 else 0

    def select_parent(self):
        weights = [bird.fitness for bird in self.birds]
        return np.random.choice(self.birds, p=weights)

    def reproduce(self):
        new_birds = []
        self.calculate_fitness()
        for _ in range(POPULATION_SIZE):
            parent = self.select_parent()
            child_brain = parent.brain.copy()
            child_brain.mutate(MUTATION_RATE)
            new_birds.append(Bird(brain=child_brain))
        self.birds = new_birds
        self.generation += 1
