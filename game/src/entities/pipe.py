from entities.physical_object import PhysicalObject
from settings import PIPE_VELOCITY

class Pipe(PhysicalObject):
    def __init__(self, hitbox, image, position):
        super().__init__(
            hitbox=hitbox,
            image=image,
            position=position,
            velocity_x=PIPE_VELOCITY,
            velocity_y=0,
            acceleration_x=0,
            acceleration_y=0
        )
