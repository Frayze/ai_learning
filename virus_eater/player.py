import pygame
from player_graphic import *
from player_brain import *

class Player:
    def __init__(self):
        self.alive = True
        self.finished = False
        self.score = 100


    def create_Graphic(self, pos, width, height, color):
        self.representation = PlayerGraphic(self, pos, width, height, color)


    def create_Brain(self):
        self.brain = PlayerBrain(self)


    def get_central_Rect(self):
        tmp = self.representation
        return pygame.Rect(tmp.pos[0] + 5, tmp.pos[1] + 5, tmp.width - 10, tmp.height - 10)


