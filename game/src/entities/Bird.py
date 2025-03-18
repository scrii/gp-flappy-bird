from entities.physical_object import PhysicalObject
from settings import JUMP_VELOCITY, FALL_ACCELERATION, BIRD_FALL_VELOCITY
from tools.bird_stats import BirdStats

class Bird(PhysicalObject):
    def __init__(self, hitbox, image, position):
        super().__init__(
            hitbox=hitbox,
            image=image,
            position=position,
            velocity_x=0,
            velocity_y=BIRD_FALL_VELOCITY,
            acceleration_x=0,
            acceleration_y=0
        )
        self.jump_start = 0
        self.is_jumped = False
        self.stats = BirdStats() # temporary?
    
    def jump(self):
        self.is_jumped = True
        self.jump_start = self._position.get_y()
        self.set_velocity_y(JUMP_VELOCITY)
        self.set_acceleration_y(FALL_ACCELERATION)

    def update(self, dt):
        super().update(dt)
        if self.is_jumped and self._position.get_y() > self.jump_start:
            self.acceleration_y = 0
            self.is_jumped = False
            self.set_velocity_y(BIRD_FALL_VELOCITY)
