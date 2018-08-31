import pygame, os, math
from player import Player
from enum import Enum
from destination import Destination


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
def check_crash(player, obstacles, goal):
    for o in obstacles:
        if player.get_central_Rect().colliderect(o.get_Rect()):
            player.alive = False
            player.score -= rect_distance(player.get_central_Rect(), goal.get_Rect())
            print("Died with score: " + str(player.score))
    player.score -= 1
    if(player.score < 0):
        player.alive = False
        print("Died from Score 0")



def rect_distance(rect_a, rect_b):
    ac = rect_a.center
    bc = rect_b.center
    dist = math.sqrt((ac[0]-bc[0])**2 - (ac[1]-bc[1])**2)

    return dist


def check_win(player, goal):
     if (player.get_central_Rect().colliderect(goal.get_Rect())):
         player.finished = True
         player.score += 200
         print("Won with score: " + str(player.score))

def game_loop():
    players = []
    obstacles = []
    goal = Destination([1000, 300], 100, 100, AppColor.GREEN.value)
    game_error = False

    while not game_error:
        gameDisplay.fill(AppColor.BLACK.value)
        pygame.draw.rect(gameDisplay, goal.color, goal.get_Rect())
        if len(players) < 10:
            ai_player = Player()

            ai_player.create_Graphic([100, 325], 50, 50, AppColor.GREEN.value)
            ai_player.representation.set_Image('orange_bacterium_small.png')
            ai_player.create_Brain()
            ai_player.score = rect_distance(goal.get_Rect(), ai_player.get_central_Rect())
            print("Start score: " + str(ai_player.score))
            players.append(ai_player)

            print("Player created")

        for p in players:
            if p.alive and not p.finished:
                p.representation.move_Player(display_width, display_height)
                draw_Player(p)
                check_crash(p, obstacles, goal)
                check_win(p, goal)
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