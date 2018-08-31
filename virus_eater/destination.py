
import pygame
class Destination:

    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color


    def get_Rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.width, self.height)


