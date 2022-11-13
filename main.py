import pygame
from player import Fighter
from functions import *

#screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#warrior and wizard sizes
WARRIOR_SIZE = 162
WARRIOR_SCALE = 3.6
WARRIOR_OFFSET = [72, 60]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 117]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

intro_count = 3
countUpdate = pygame.time.get_ticks()
FPS = 60

#INITIATION
pygame.init()
pygame.display.set_caption("Fighter")

#step definition
WARRIOR_ANIMATION_LIST = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_LIST = [8, 8, 1, 8, 8, 3, 7]

#SCREEN_DISPLAY
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

#load font
count_font = pygame.font.Font("graphics/Font/turok.ttf", 80)
score_font = pygame.font.Font("graphics/Font/turok.ttf", 30)

#load spritesheets
warrior_sheet = pygame.image.load("graphics\warrior_sprites\warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("graphics\wizard_sprites\wizard.png").convert_alpha()

#FIGHTERS
player1 = Fighter(1, 200, 420, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_LIST)
player2 = Fighter(2, 700, 420, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_LIST)


background = pygame.image.load("graphics/bg.jpg").convert_alpha()


while run:
    #DISPLAY Background
    draw_background(screen, background, SCREEN_WIDTH, SCREEN_HEIGHT)

    #DRAW HEALTH BARS
    draw_health_bar(player1.health, screen, 20, 40)
    draw_health_bar(player2.health, screen, 580, 40)
    if intro_count <= 0:
        player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2)
        player2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player1)
    else:
        if (pygame.time.get_ticks() - countUpdate) >= 1000:
            intro_count -= 1
            countUpdate = pygame.time.get_ticks()
            print(intro_count+1)

    #DISPLAY Fighters
    player1.update()
    player2.update()

    player1.draw(screen)
    player2.draw(screen)

    qkey = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if qkey[pygame.K_LCTRL]:
            if qkey[pygame.K_w]:
                run = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()