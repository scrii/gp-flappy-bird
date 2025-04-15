class Hitbox:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height