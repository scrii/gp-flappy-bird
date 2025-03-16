from enum import Enum

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
FPS = 30
ASSETS_PATH = '../assets/'

class Color(Enum):
    WHITE = (255, 255, 255)

FALL_ACCELERATION = 1.8
JUMP_VELOCITY = -17

PIPE_VELOCITY = -6.2
PIPE_MIN_HEIGHT = SCREEN_HEIGHT // 5
PIPES_HORIZONTAL_GAP = SCREEN_WIDTH // 2.5

BIRD_SIZE = SCREEN_HEIGHT // 10
PIPE_WIDTH = BIRD_SIZE * 1.6
PIPES_VERTICAL_GAP = int(2.8 * BIRD_SIZE)

BIRD_FALL_VELOCITY = -JUMP_VELOCITY