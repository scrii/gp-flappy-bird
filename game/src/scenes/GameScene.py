import pygame
from settings import Color
from entities.Bird import Bird
from entities.GraphicsObject import GraphicsObject
from gp import GeneticProgramming

class GameScene:
    def __init__(self, game):
        self.game = game
        self.birds = GeneticProgramming.initialize_population()
    
    def handle_event(self, event):
        pass

    def update(self, dt):
        for bird in self.birds:
            bird.update()

    def draw(self, screen):
        screen.fill(Color.WHITE.value)
        for bird in self.birds:
            bird.draw(screen)