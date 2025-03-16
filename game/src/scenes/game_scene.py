import pygame
from settings import Color
from entities.bird import Bird
from entities.graphics_object import GraphicsObject
from gp import GeneticProgramming
from scenes.scene import Scene
from entities.physical_object import PhysicalObject
from tools.hitbox import Hitbox
from tools.point import Point
from settings import ASSETS_PATH, PIPES_HORIZONTAL_GAP, SCREEN_WIDTH, SCREEN_HEIGHT, BIRD_SIZE
from entities.pipe import Pipe
from entities.composite_pipe import CompositePipe

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.player = Bird(Hitbox(BIRD_SIZE, BIRD_SIZE), pygame.image.load(ASSETS_PATH + 'images/bird.png'), Point(0, 0))
        self.add_graphics_object(
            self.player
        )
        composite_pipe = CompositePipe(
            image=pygame.image.load(ASSETS_PATH + 'images/pipe.png')
        )
        self.add_graphics_object(composite_pipe.lower_pipe)
        self.add_graphics_object(composite_pipe.upper_pipe)
        self.pipes = [composite_pipe.lower_pipe, composite_pipe.upper_pipe]
        self.birds = [self.player]

    def process_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player.jump()

    def update(self, dt):
        super().update(dt)
        if self.pipes and SCREEN_WIDTH - self.pipes[-1]._position.get_x() > PIPES_HORIZONTAL_GAP:
            composite_pipe = CompositePipe(
                image=pygame.image.load(ASSETS_PATH + 'images/pipe.png')
            )
            self.pipes.append(composite_pipe.lower_pipe)
            self.pipes.append(composite_pipe.upper_pipe)
            self.add_graphics_object(composite_pipe.lower_pipe)
            self.add_graphics_object(composite_pipe.upper_pipe)

        for pipe in self.pipes:
            if self.player.check_collision(pipe):
                # Reset run_condition
                
                pass
            if pipe.check_off_screen():
                self.remove_graphics_object(self.pipes.pop(0))
