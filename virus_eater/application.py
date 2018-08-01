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
pygame.display.set_caption("Virus Eater")

clock = pygame.time.Clock()
rand = random.Random()


def draw_Player(player):
    if player.alive:
        gameDisplay.blit(player.representation.get_Fill(), player.representation.get_Edges())

    
def get_player_killed(player, main_player):
    if(player.get_central_Rect().colliderect(main_player.get_central_Rect())):
        player.alive = False
        print("Died with score: " + str(player.score))
    else:
        player.score += 1
    








def game_loop():

    players = []
    p1 = Player()
    p1.create_Graphic(0, 0, 100, 100, AppColor.RED.value)
    p1.representation.set_Image('orange_bacterium_small.png')
    p1.create_Brain()
    game_error = False

    while not game_error:
        gameDisplay.fill(AppColor.BLACK.value)
        if len(players) < 10:
            ai_player = Player()
            rand_x = rand.randint(0, display_width)
            rand_y = rand.randint(0, display_width)

            ai_player.create_Graphic(rand_x, rand_y, 50, 50, AppColor.GREEN.value)
            ai_player.representation.set_Image('orange_bacterium_small.png')
            ai_player.create_Brain()

            players.append(ai_player)

        for p in players:
            if p.alive:
                p.representation.random_move(rand, display_width, display_height)
                get_player_killed(p, p1)
                draw_Player(p)
            else:
                players.remove(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p1.representation.x_speed = -10
                elif event.key == pygame.K_RIGHT:
                    p1.representation.x_speed = 10
                elif event.key == pygame.K_DOWN:
                    p1.representation.y_speed = 10
                elif event.key == pygame.K_UP:
                    p1.representation.y_speed = -10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    p1.representation.x_speed = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    p1.representation.y_speed = 0
        p1.representation.move_Player(display_width, display_height)
        pygame.draw.rect(gameDisplay, AppColor.RED.value, p1.representation.get_Rect())
        pygame.display.update()
        clock.tick(50)
game_loop()
pygame.quit()
quit()