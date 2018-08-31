import pygame, os
from player import Player
from enum import Enum

import random

class AppColor(Enum):
	BLACK = (0,0,0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255) 



os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

display_width = 1200
display_height = 700

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Virus Eater")

clock = pygame.time.Clock()
rand = random.Random()


def draw_Player(player):
    if player.alive:
        gameDisplay.blit(player.representation.get_Fill(), player.representation.get_Edges())



#Deprecated
def get_player_killed(player, main_player):
    if(player.get_central_Rect().colliderect(main_player.get_central_Rect())):
        player.alive = False
        print("Died with score: " + str(player.score))
    else:
        player.score += 1
    

def game_loop():
    players = []

    game_error = False

    while not game_error:
        gameDisplay.fill(AppColor.BLACK.value)
        if len(players) < 10:
            ai_player = Player()

            rand_y = rand.randint(0, display_height)
            ai_player.create_Graphic([100, rand_y], 50, 50, AppColor.GREEN.value)
            ai_player.representation.set_Image('orange_bacterium_small.png')
            ai_player.create_Brain()
            players.append(ai_player)

            print("Player created")

        for p in players:
            if p.alive:
                p.representation.move_Player(display_width, display_height)
                draw_Player(p)
            else:
                players.remove(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(50)
game_loop()
pygame.quit()
quit()