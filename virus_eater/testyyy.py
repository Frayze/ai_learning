import pygame

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("KI Learning Simulation")
clock = pygame.time.Clock()

bacterium_img1 = pygame.image.load('orange_bacterium_small.png').convert()

asd = pygame.Rect(200,200,100,100)

while True:
    gameDisplay.fill((0,0,0))
    gameDisplay.blit(bacterium_img1, asd)
    asd[0] += 1
    asd[1] += 1

    pygame.display.update()
    clock.tick(40)
