
import pygame

class PlayerGraphic:

    def __init__(self, player, pos_x, pos_y, width, height, color = (0,22,0)):
        self.x_speed = 0
        self.y_speed = 0
        self.player = player
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height


    def get_Rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)


    def get_Edges(self):
        return (self.pos_x, self.pos_y)


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
        # check x
        if self.pos_x + self.x_speed < 0:
            self.pos_x = 0
            self.x_speed = 0
        elif self.pos_x + self.x_speed + self.width > display_width:
            self.pos_x = display_width - self.width
            self.x_speed = 0
        else:
            self.pos_x += self.x_speed
        # check y
        if self.pos_y + self.y_speed < 0:
            self.pos_y = 0
            self.y_speed = 0
        elif self.pos_y + self.y_speed + self.height > display_height:
            self.pos_y = display_height - self.height
            self.y_speed = 0
        else:
            self.pos_y += self.y_speed


    def random_move(self, rand, display_width, display_height):
        if self.x_speed > 0:
            self.x_speed = rand.randint(0, 7)
        elif self.x_speed < 0:
            self.x_speed = rand.randint(-7, 0)
        else:
            self.x_speed = rand.randint(-7, 7)

        if self.y_speed > 0:
            self.y_speed = rand.randint(0, 7)
        elif self.y_speed < 0:
            self.y_speed = rand.randint(-7, 0)
        else:
            self.y_speed = rand.randint(-10, 10)

        self.move_Player(display_width, display_height)