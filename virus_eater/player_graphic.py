
import pygame


class PlayerGraphic:

    def __init__(self, player, pos, width, height, color = (0,0,0)):
        self.player = player
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height

    def get_Rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)


    def get_Edges(self):
        return [self.pos[0], self.pos[1]]


    def set_Image(self, imagepath):
        img = pygame.image.load(imagepath).convert_alpha()
        alpha_surface = pygame.Surface(img.get_size(), pygame.SRCALPHA)
        alpha_surface.fill((255, 255, 255, 90))
        img.blit(alpha_surface, (0,0), special_flags=pygame.BLEND_RGB_MULT)
        self.img = img


    def get_Fill(self):
        if hasattr(self, 'img'):
            return self.img
        else:
            return self.color


    def move_Player(self, display_width, display_height):
        move = self.player.brain.get_move()
        # check x
        if self.pos[0] + move[0] < 0:
            self.pos[0] = 0

        elif self.pos[0] + move[0] + self.width > display_width:
            self.pos[0] = display_width - self.width

        else:
            self.pos[0] += move[0]


        # check y
        if self.pos[1] + move[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] + move[1] + self.height > display_height:
            self.pos[1] = display_height - self.height
        else:
            self.pos[1] += move[1]


