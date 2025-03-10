import pygame.locals
from entities.Bird import Bird
from entities.GraphicsObject import GraphicsObject
from typing import List
from settings import *
import pygame


class GeneticProgramming:
    def __init__(self):
        pass

    @staticmethod
    def initialize_population() -> List[Bird]:
        return [Bird((100,50), pygame.image.load(ASSETS_PATH + 'images/bird.png'), (0, 0))]