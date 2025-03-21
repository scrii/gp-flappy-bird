import pygame.locals
from entities.Bird import Bird
from entities.gp_bird import GPBird
from entities.graphics_object import GraphicsObject
from typing import List
from settings import *
import pygame
import random


class GeneticProgramming:
    def __init__(self, population_size: int, mutation_rate: float, crossover_rate: float, tournament_size: int, population: List[GPBird]):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.tournament_size = tournament_size
        self.population = [bird.get_decision_tree() for bird in population]
        pass

    def evolve(self):
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = self.selection()
            if random.random() < self.crossover_rate:
                offspring = self.crossover(parent1, parent2)
            else:
                offspring = parent1 if random.random() < 0.5 else parent2
            if random.random() < self.mutation_rate:
                self.mutate(offspring)
            new_population.append(offspring)
        self.population = new_population

    def selection(self):
        tournament = random.sample(self.population, self.tournament_size)
        return sorted(tournament, key=lambda x: x.fitness, reverse=True)[:2]

    def crossover(self, parent1, parent2):
        # TODO
        offspring = ...
        return offspring

    def mutate(self, tree):
        # TODO
        pass

