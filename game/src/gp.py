import copy
from random import choice
import pygame.locals
from entities.Bird import Bird
from entities.gp_bird import GPBird
from entities.graphics_object import GraphicsObject
from typing import List
from entities.DecisionTreeNode import *
from tools.hitbox import Hitbox
from tools.point import Point
from settings import *
import pygame
import random


class GeneticProgramming:
    def __init__(self, population_size: int=10, mutation_rate: float=0.05, crossover_rate: float=0.95, tournament_size: int=5, population: List[GPBird]=None) -> None:
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.tournament_size = tournament_size
        self.population = population
        #pass

    def evolve(self) -> List[GPBird]:
        new_population = []
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        for i in range(5): # save 5 the best
            offspring = copy.copy(self.population[i].get_decision_tree())
            new_population.append(GPBird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + f'images/{choice(BIRDTEXTURES)}.png'),
                              Point(BIRD_X_POSITION, 0), decision_tree=offspring))
        while len(new_population) < self.population_size:
            parent1, parent2 = self.selection()
            if random.random() < self.crossover_rate:
                offspring = self.crossover(parent1.get_decision_tree(), parent2.get_decision_tree())
            else:
                offspring = parent1.get_decision_tree() if random.random() < 0.5 else parent2.get_decision_tree()
            if random.random() < self.mutation_rate:
                offspring = self.mutate(offspring)
            bird = GPBird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + f'images/{choice(BIRDTEXTURES)}.png'),
                              Point(BIRD_X_POSITION, 0), decision_tree=offspring)
            if bird.get_decision_tree().get_tree_depth() > 10: continue
            else: new_population.append(bird)
        self.population = new_population
        return new_population

    def selection(self):
        tournament = random.sample(self.population, self.tournament_size)
        return sorted(tournament, key=lambda x: x.fitness, reverse=True)[:2]

    def crossover(self, parent1, parent2):
        node1 = get_random_node(parent1)
        node2 = get_random_node(parent2)
        if random.random() < 0.5:
            new_branch = node1
            old_branch = node2
            offspring = parent2
        else:
            new_branch = node2
            old_branch = node1
            offspring = parent1
        offspring = replace_node(offspring, old_branch, new_branch)
        return offspring

    def mutate(self, tree):
        old_node = get_random_node(tree)
        new_node = generate_random_tree()
        tree = replace_node(tree, old_node, new_node)
        return tree

