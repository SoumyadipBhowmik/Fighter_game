import pygame
from player import Fighter
from functions import *
#COLOR
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255,255,255)

#SCREEN SIZE
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#king, warrior and wizard sizes
KING_SIZE = 162.1
KING_SCALE = 3
KING_OFFSET = [75,58]
KING_DATA = [KING_SIZE, KING_SCALE, KING_OFFSET]

WARRIOR_SIZE = 162
WARRIOR_SCALE = 3.8
WARRIOR_OFFSET = [72, 60]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 117]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

intro_count = 3
countUpdate = pygame.time.get_ticks()


score = [0, 0] #player scores P1/P2
roundOver = False
ROUND_OVER_COOLDOWN = 2000

FPS = 60

#INITIATION
pygame.init()
pygame.display.set_caption("Fighter")

#step definition
WARRIOR_ANIMATION_LIST = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_LIST = [8, 8, 1, 8, 8, 3, 7]
KING_ANIMATION_LIST = [8, 8, 2, 4, 4, 4, 6]

#SCREEN_DISPLAY
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

#load font
count_font = pygame.font.Font("graphics/Font/turok.ttf", 80)
score_font = pygame.font.Font("graphics/Font/turok.ttf", 30)

#load spritesheets
king_sheet = pygame.image.load("graphics\king_sprites\king.png").convert_alpha()
warrior_sheet = pygame.image.load("graphics\warrior_sprites\warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("graphics\wizard_sprites\wizard.png").convert_alpha()
victoryImg = pygame.image.load("graphics/Font/victory.png").convert_alpha()

#FIGHTERS
player1 = Fighter(1, 200, 420, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_LIST)
player2 = Fighter(2, 720, 420, True, KING_DATA, king_sheet, KING_ANIMATION_LIST)


background = pygame.image.load("graphics/bg.jpg").convert_alpha()


while run:
    #DISPLAY Background
    draw_background(screen, background, SCREEN_WIDTH, SCREEN_HEIGHT)

    #DRAW HEALTH BARS
    draw_health_bar(player1.health, screen, 20, 40)
    draw_health_bar(player2.health, screen, 580, 40)
    text(screen, "P1: " +str(score[0]), score_font, RED, 20,80)
    text(screen, "P2: " + str(score[1]), score_font, RED, 900, 80)


    if intro_count <= 0:
        player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2, roundOver)
        player2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player1, roundOver)
    else:
        text(screen, str(intro_count), count_font, RED, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        if (pygame.time.get_ticks() - countUpdate) >= 1000:
            intro_count -= 1
            countUpdate = pygame.time.get_ticks()


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

    #check for player defeat
    if roundOver == False:
        if player1.alive == False:
            score[1] += 100
            roundOver = True
            roundOver_time = pygame.time.get_ticks()
        elif player2.alive == False:
            score[0] += 100
            roundOver = True
            roundOver_time = pygame.time.get_ticks()
    else:
        screen.blit(victoryImg, (350, SCREEN_HEIGHT/2))
        if pygame.time.get_ticks() - roundOver_time > ROUND_OVER_COOLDOWN:
            roundOver = False
            intro_count = 3
            player1 = Fighter(1, 200, 420, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_LIST)
            player2 = Fighter(2, 700, 420, True, KING_DATA, king_sheet, KING_ANIMATION_LIST)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()