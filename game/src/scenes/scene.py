from abc import ABC, abstractmethod
from entities.graphics_object import GraphicsObject
from settings import *
import pygame

class Scene(ABC):
    def __init__(self):
        self.graphics_objects = []

    def draw(self, screen: pygame.surface.Surface):
        screen.fill((0, 0, 0))
        for graphics_object in self.graphics_objects:
            graphics_object.draw(screen)
        pygame.display.flip()

    def update(self, dt):
        for graphics_object in self.graphics_objects:
            graphics_object.update(dt)
    
    @abstractmethod
    def process_event(self, event: pygame.event.Event):
        pass

    def add_graphics_object(self, graphics_object: GraphicsObject):
        self.graphics_objects.append(graphics_object)
    
    def remove_graphics_object(self, graphics_object: GraphicsObject):
        self.graphics_objects.remove(graphics_object)