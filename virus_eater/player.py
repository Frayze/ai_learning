import pygame
from player_graphic import *
from player_brain import *
import copy

class Player:
    def __init__(self):
        self.alive = True
        self.finished = False
        self.score = 925


    def create_Graphic(self, pos, width, height, color):
        self.representation = PlayerGraphic(self, pos, width, height, color)


    def create_Brain(self):
        self.brain = PlayerBrain(self)


    def get_central_Rect(self):
        tmp = self.representation
        return pygame.Rect(tmp.pos[0] + 5, tmp.pos[1] + 5, tmp.width - 10, tmp.height - 10)

    @staticmethod
    def create_generation(players):
        size = len(players)
        print("generationsize: " + str(size))
        fittest = PlayerBrain.selection(players)
        print("Fittest selected")

        mutual = 0
        new_players = []
        for i in range(size):
            new = fittest[mutual].clonePlayer()
            new.brain.mutate(0.1)
            new_players.append(new)
            mutual = (mutual + 1) % len(fittest)
        print("Population copied, mutated and reset")
        return new_players

    def clonePlayer(self):
        graphic = self.representation
        self.brain.step = 0
        brain = copy.deepcopy(self.brain)
        p = Player()
        p.create_Graphic([100, 325], 50, 50, (0,255,0))
        p.representation.set_Image('orange_bacterium_small.png')
        p.brain = brain

        return p