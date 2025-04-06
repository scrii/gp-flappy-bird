import pygame

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
            self.current_scene.process_event(event)
    
    def update(self, dt):
        self.current_scene.update(dt)
        if len(self.current_scene.birds) == 0:

            oldPop = self.current_scene.geneticProgramming.population
            oldPop.sort(key=lambda x: x.fitness, reverse=True)
            print(oldPop[0].fitness)
            print('new gen')
            # create new generation
            newBirds = self.current_scene.geneticProgramming.evolve()
            population = []
            for _ in range(len(newBirds)):
                # bird = GPBird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + 'images/bird.png'),
                #               Point(BIRD_X_POSITION, 0), decision_tree=newBrains[_])
                population.append(newBirds[_])
            # update environment
            del self.current_scene
            self.current_scene = GameScene(population)
            #self.current_scene.birds = population

    def draw(self):
        self.current_scene.draw(self.screen)
        pygame.display.flip()
