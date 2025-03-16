from entities.graphics_object import GraphicsObject
from settings import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, FALL_ACCELERATION
from math import sqrt

class PhysicalObject(GraphicsObject):
    def __init__(self, hitbox, image, position, velocity_x = 0, velocity_y = 0, acceleration_x = 0, acceleration_y = FALL_ACCELERATION):
        super().__init__(hitbox, image, position)
        self._velocity_x = velocity_x
        self._velocity_y = velocity_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
    
    def draw(self, screen):
        super().draw(screen)
    
    def update(self, dt):
        self.add_velocity_x(self.acceleration_x * dt * FPS)
        self.add_velocity_y(self.acceleration_y * dt * FPS)
        self._position.add(self._velocity_x, self._velocity_y)
    
    def add_velocity_x(self, dv_x):
        self._velocity_x += dv_x

    def add_velocity_y(self, dv_y):
        self._velocity_y += dv_y

    def set_velocity_x(self, velocity_x):
        self._velocity_x = velocity_x

    def set_velocity_y(self, velocity_y):
        self._velocity_y = velocity_y

    def set_acceleration_x(self, acceleration_x):
        self.acceleration_x = acceleration_x

    def set_acceleration_y(self, acceleration_y):
        self.acceleration_y = acceleration_y

    def get_distance(self, object: "PhysicalObject"):
        return sqrt((self._position.get_x() - object._position.get_x())**2 + 
                    (self._position.get_y() - object._position.get_y())**2)

    def check_collision(self, object: 'PhysicalObject'):
        left1 = min(self._position.get_x(), self._position.get_x() + self._hitbox.get_width())
        right1 = max(self._position.get_x(), self._position.get_x() + self._hitbox.get_width())
        top1 = min(self._position.get_y(), self._position.get_y() + self._hitbox.get_height())
        bottom1 = max(self._position.get_y(), self._position.get_y() + self._hitbox.get_height())

        left2 = min(object._position.get_x(), object._position.get_x() + object._hitbox.get_width())
        right2 = max(object._position.get_x(), object._position.get_x() + object._hitbox.get_width())
        top2 = min(object._position.get_y(), object._position.get_y() + object._hitbox.get_height())
        bottom2 = max(object._position.get_y(), object._position.get_y() + object._hitbox.get_height())

        return (left1 < right2 and left2 < right1) and (top1 < bottom2 and top2 < bottom1)

    def check_off_screen(self):
        return (
            self._position.get_x() + self._hitbox.get_width() < 0 or
            self._position.get_x() > SCREEN_WIDTH or
            self._position.get_y() + self._hitbox.get_height() < 0 or
            self._position.get_y() > SCREEN_HEIGHT
        )
