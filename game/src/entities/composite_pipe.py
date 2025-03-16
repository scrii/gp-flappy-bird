from entities.pipe import Pipe
import random
from settings import PIPE_MIN_HEIGHT, PIPES_VERTICAL_GAP
from tools.hitbox import Hitbox
from tools.point import Point
from settings import PIPE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class CompositePipe:
    def __init__(self, image):
        lower_pipe_y = SCREEN_HEIGHT - random.randint(PIPE_MIN_HEIGHT, PIPE_MIN_HEIGHT + PIPES_VERTICAL_GAP)
        self.lower_pipe = Pipe(
            hitbox=Hitbox(PIPE_WIDTH, SCREEN_HEIGHT - lower_pipe_y),
            image=image,
            position=Point(SCREEN_WIDTH, lower_pipe_y)
        )
        upper_pipe_height = lower_pipe_y - PIPES_VERTICAL_GAP
        self.upper_pipe = Pipe(
            hitbox=Hitbox(PIPE_WIDTH, upper_pipe_height),
            image=pygame.transform.flip(image, False, True),
            position=Point(SCREEN_WIDTH, 0)
        )