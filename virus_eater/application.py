import pygame
from player import Player
from enum import Enum

import random

class AppColor(Enum):
	BLACK = (0,0,0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255) 

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("KI Learning Simulation")

clock = pygame.time.Clock()
rand = random.Random()
#Create Moving Image
#bacterium_img1 = pygame.image.load('orange_bacterium_small.png').convert()	
#def bacterium (x, y):
#        gameDisplay.blit(bacterium_img1, (x,y))

def draw_Player(player):
    if player.alive:
        gameDisplay.blit(player.representation.get_Fill(), player.representation.get_Rect())


def move_Player(player):
    #check x
    if player.pos_x + player.x_speed < 0:
        player.pos_x = 0
        player.x_speed = 0
    elif player.pos_x + player.x_speed + player.width > display_width:
        player.pos_x = display_width - player.width
        player.x_speed = 0
    else:
        player.pos_x += player.x_speed
    #check y
    if player.pos_y + player.y_speed < 0:
        player.pos_y = 0
        player.y_speed = 0
    elif player.pos_y + player.y_speed + player.height > display_height:
        player.pos_y = display_height - player.height
        player.y_speed = 0
    else:
        player.pos_y += player.y_speed
    
def get_player_killed(player, main_player):
    if(player.get_Rect().colliderect(main_player.get_Rect())):
        player.alive = False
        print("Died with score: " + str(player.score))
    else:
        player.score += 1
    
def random_move(player, main_player):
    if player.x_speed > 0:
        player.x_speed = rand.randint(0,5)
    elif player.x_speed < 0:
        player.x_speed = rand.randint(-5, 0)
    else:
        player.x_speed = rand.randint(-5,5)
    
    if player.y_speed > 0:
        player.y_speed = rand.randint(0,5)
    elif player.y_speed < 0:
        player.y_speed = rand.randint(-5, 0)
    else:
        player.y_speed = rand.randint(-5,5)
    
    move_Player(player)


    
def game_loop():
    gameDisplay.fill(AppColor.BLACK.value)

    p1 = Player()
    p1.create_Graphic(0, 0, 100, 100, AppColor.RED.value)
    p1.representation.set_Image('orange_bacterium_small.png')
    p1.create_Brain()
    game_error = False

    while not game_error:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #print(event)  Debugging
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_UP:
                    pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    pass
        pygame.display.update() #Kann eventuell nur ein Objekt (Parameter) updaten. Kann auch mit display.flip() erreicht werden
        clock.tick(50)
game_loop()
pygame.quit()
quit()