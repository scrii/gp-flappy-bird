import pygame
from random import choice
from entities.Bird import Bird
from entities.gp_bird import GPBird
from entities.graphics_object import GraphicsObject
from gp import GeneticProgramming
from scenes.scene import Scene
from entities.physical_object import PhysicalObject
from tools.hitbox import Hitbox
from tools.point import Point
from settings import ASSETS_PATH, PIPES_HORIZONTAL_GAP, SCREEN_WIDTH, SCREEN_HEIGHT, BIRD_SIZE, BIRD_X_POSITION, PIPE_WIDTH
from entities.pipe import Pipe
from entities.composite_pipe import CompositePipe

from settings import PIPE_MIN_HEIGHT, PIPES_VERTICAL_GAP, BIRDTEXTURES


class GameScene(Scene):
    def __init__(self, population = None):
        super().__init__()
        self.reached_pipes = 0
        # self.player = Bird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + 'images/bird.png'), Point(BIRD_X_POSITION, 0))
        # self.add_graphics_object(
        #     self.player
        # )
        # self.birds = [self.player]
        if population is None:
            population = []
            for _ in range(100):
                bird = GPBird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + f'images/{choice(BIRDTEXTURES)}.png'), Point(BIRD_X_POSITION, 0))
                population.append(bird)

        for bird in population:
            self.add_graphics_object(bird)
        self.birds = [bird for bird in population]
        self.pipes = []
        self.generate_composite_pipe()
        self.next_pipe = self.pipes[0]
        self.is_next_pipe_added = True
        self.geneticProgramming = GeneticProgramming(population=population, population_size=100, mutation_rate=0.2, tournament_size=30)


    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # self.player.jump()
                pass

    def update(self, dt):
        super().update(dt)
        if self.pipes and SCREEN_WIDTH - self.pipes[-1]._position.get_x() > PIPES_HORIZONTAL_GAP:
            self.generate_composite_pipe()

        if self.is_next_pipe_added and \
            self.birds and self.next_pipe._position.get_x() + PIPE_WIDTH - self.birds[0]._position.get_x() <= 0:
                self.reached_pipes += 1
                self.is_next_pipe_added = False
                #print("reached")


        for pipe in self.pipes:
            if pipe.check_off_screen():
                self.remove_graphics_object(self.pipes.pop(0))
            if not self.is_next_pipe_added and \
                self.birds and pipe._position.get_x() + PIPE_WIDTH - self.birds[0]._position.get_x() > 0:
                self.next_pipe = pipe
                self.is_next_pipe_added = True
                #print("pipe is switched")
                for bird in self.birds:
                    bird.fitness += 20
            
        for bird in self.birds:
            if bird.check_off_screen():
                bird.stats.set_score(
                    bird.fitness
                    #self.reached_pipes
                )
                self.birds.remove(bird)
                self.remove_graphics_object(bird)

        for bird in self.birds:
            for pipe in self.pipes:
                if bird.check_collision(pipe):
                    bird.stats.set_score(
                        bird.fitness
                    )
                    self.birds.remove(bird)
                    self.remove_graphics_object(bird)

        for gp_bird in self.birds:
            # get next_pipe position and make decision
            if gp_bird.make_decision(terminal_set=[gp_bird._position.get_x(), gp_bird._position.get_y(), self.next_pipe._position.get_x(), self.next_pipe._position.get_y() ]):
                gp_bird.jump()

        for bird in self.birds:
            bird.fitness += 1 # bonus for lifetime
            # bonus for being close to gap
            bird.fitness += 100 / (abs( self.next_pipe._position.get_y() + PIPES_VERTICAL_GAP / 2 - bird._position.get_y()) + 3)
            if bird._position.get_y() < SCREEN_HEIGHT - PIPE_MIN_HEIGHT - PIPES_VERTICAL_GAP or bird._position.get_y() > SCREEN_HEIGHT - PIPE_MIN_HEIGHT:
                # debuff for being close to borders
                bird.fitness -= 1





    
    def generate_composite_pipe(self):
        composite_pipe = CompositePipe(
                image=pygame.image.load(ASSETS_PATH + 'images/pipe.png')
            )
        self.pipes.append(composite_pipe.lower_pipe)
        self.pipes.append(composite_pipe.upper_pipe)
        self.add_graphics_object(composite_pipe.lower_pipe)
        self.add_graphics_object(composite_pipe.upper_pipe)
