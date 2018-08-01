import pygame
from player_graphic import *
from player_brain import *


class Player:
    def __init__(self):
        self.alive = True
    def create_Graphic(self, color, pos_x, pos_y, width, height):
        self.representation = PlayerGraphic(self, color, pos_x, pos_y, width, height)


    def create_Brain(self):
        self.brain = PlayerBrain(self)


    def get_central_Rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)


