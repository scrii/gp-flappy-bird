import pygame
from settings import *
from scenes.GameScene import GameScene

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.current_scene = GameScene(self)
        self.clock = pygame.time.Clock()
        self.run_condition = True
    
    def run(self):
        while self.run_condition:
            self.process_events()
            self.update()
            self.draw()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            self.current_scene.handle_event(event)
    
    def update(self):
        self.current_scene.update(self.clock.tick(FPS) / 1000)

    def draw(self):
        self.current_scene.draw(self.screen)
        pygame.display.flip()