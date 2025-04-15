import pygame
from random import choice
from entities.gp_bird import GPBird
from tools.hitbox import Hitbox
from tools.point import Point
from settings import *
from scenes.game_scene import GameScene
import time

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.current_scene = GameScene()
        self.clock = pygame.time.Clock()
        self.run_condition = True
        self.is_paused = False
        self.reset_counter = 0
        self.prev_fitness = 0
        self.reset_condition = 10
        with open("output.txt", "w"):
            pass

    def run(self):
        prev_time = time.time()
        while self.run_condition:
            self.clock.tick(FPS)
            now_time = time.time()
            dt = now_time - prev_time
            prev_time = now_time

            self.process_events()
            if not self.is_paused:
                self.update(dt)
                self.draw()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_condition = False
                break
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(
                    (event.w, event.h), 
                    pygame.RESIZABLE
                )
                break
            elif event.type == pygame.ACTIVEEVENT:
                self.is_paused = (event.gain == 0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    population = self.reset_population()
                    self.restart(population)
            self.current_scene.process_event(event)
    
    def update(self, dt):
        self.current_scene.update(dt)
        if len(self.current_scene.birds) == 0:
            oldPop = self.current_scene.geneticProgramming.population
            oldPop.sort(key=lambda x: x.fitness, reverse=True)
            if oldPop[0].fitness > self.prev_fitness:
                self.reset_counter = 0
            else:
                self.reset_counter += 1
            self.prev_fitness = oldPop[0].fitness
            print(self.prev_fitness)
            with open("output.txt", "a") as f:
                f.write(f"{self.prev_fitness}\n")

            # create new generation
            if self.reset_counter == self.reset_condition:
                population = self.reset_population()
            else:
                newBirds = self.current_scene.geneticProgramming.evolve()
                population = []
                for _ in range(len(newBirds)):
                    population.append(newBirds[_])
            # update environment
            self.restart(population)
            #self.current_scene.birds = population

    def reset_population(self):
        print('RESET')
        with open("output.txt", "a") as f:
            f.write(f"RESET\n")
        population = []
        for _ in range(100):
            bird = GPBird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + f'images/{choice(BIRDTEXTURES)}.png'),
                          Point(BIRD_X_POSITION, 0))
            population.append(bird)
        return population
    
    def restart(self, population):
        del self.current_scene
        self.current_scene = GameScene(population)

    def draw(self):
        self.current_scene.draw(self.screen)
        pygame.display.flip()
