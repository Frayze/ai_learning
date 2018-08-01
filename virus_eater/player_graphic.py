
import pygame

class PlayerGraphic:

    def __init__(self, player, pos_x, pos_y, width, height, color = (0,22,0)):
        self.player = player
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def get_Rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)


    def set_Image(self, imagepath):
        self.img = pygame.image.load(imagepath).convert()


    def get_Fill(self):
        if hasattr(self, 'img'):
            return self.img
        else:
            return self.color


    def get_image_start(self):
        return (self.pos_x - 5, self.pos_y - 5)