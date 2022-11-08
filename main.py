import pygame
from player import Fighter
from background import draw_background

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

#INITIATION
pygame.init()
pygame.display.set_caption("Fighter")

#SCREEN_DISPLAY
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

#FIGHTERS
player1 = Fighter(200,420)
player2 = Fighter(700, 420)


background = pygame.image.load("graphics/bg.jpg").convert_alpha()
while run:
    #DISPLAY Background
    draw_background(screen, background, SCREEN_WIDTH, SCREEN_HEIGHT)

    #DISPLAY Fighters
    player1.draw(screen)
    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.K_a, pygame.K_d, pygame.K_w, screen)
    player2.draw(screen)
    player2.move(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()