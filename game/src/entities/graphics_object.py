from abc import ABC, abstractmethod
import pygame
from tools.point import Point
from tools.hitbox import Hitbox
from math import sqrt

class GraphicsObject(ABC):
    def __init__(self, hitbox: Hitbox, image: pygame.image, position: Point):
        self._hitbox = hitbox
        self._image = pygame.transform.scale(
            image,
            (self._hitbox.get_width(), self._hitbox.get_height())
        )
        self._position = position
    
    @abstractmethod
    def update(self, dt):
        pass

    def get_distance(self, object: "GraphicsObject"):
        return sqrt((self._position.get_x() - object._position.get_x())**2 + 
                    (self._position.get_y() - object._position.get_y())**2)

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self._image, self._position.get_tuple())
    