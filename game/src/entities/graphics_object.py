from typing import Tuple
from abc import ABC, abstractmethod
import pygame

class GraphicsObject(ABC):
    def __init__(self, hitbox: Tuple[int, int], image: pygame.image, position: Tuple[int, int]):
        self.hitbox = hitbox
        self.image = image
        self.position = position
    
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.position)