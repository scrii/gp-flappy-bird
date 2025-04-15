class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
    
    def add(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def get_tuple(self):
        return (self.__x, self.__y)