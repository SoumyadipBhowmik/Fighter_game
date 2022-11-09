import pygame
from player import Fighter
from functions import draw_health_bar
from functions import draw_background

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

    #DRAW HEALTH BARS
    draw_health_bar(player1.health, screen, 20, 40)
    draw_health_bar(player2.health, screen, 580, 40)
    #DISPLAY Fighters
    player1.draw(screen)
    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.K_a, pygame.K_d, pygame.K_w, screen, player2)
    player2.draw(screen)
    player2.move(SCREEN_WIDTH, SCREEN_HEIGHT, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, screen, player1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()