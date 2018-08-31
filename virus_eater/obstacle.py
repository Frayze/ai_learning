import pygame

class Obstacle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_Rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
