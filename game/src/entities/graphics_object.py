from abc import ABC, abstractmethod
import pygame
from tools.point import Point
from tools.hitbox import Hitbox

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

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self._image, self._position.get_tuple())
    