import pygame
from player_graphic import *
from player_brain import *

class Player:
    def __init__(self):
        self.alive = True
        self.score = 0


    def create_Graphic(self, color, pos_x, pos_y, width, height):
        self.representation = PlayerGraphic(self, color, pos_x, pos_y, width, height)


    def create_Brain(self):
        self.brain = PlayerBrain(self)


    def get_central_Rect(self):
        tmp = self.representation
        return pygame.Rect(tmp.pos_x + 5, tmp.pos_y + 5, tmp.width - 10, tmp.height - 10)


