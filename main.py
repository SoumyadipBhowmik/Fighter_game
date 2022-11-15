import pygame
from pygame import mixer
from player import Fighter
from functions import *
from characters import *
from sounds import *

intro_count = 3
countUpdate = pygame.time.get_ticks()

score = [0, 0] #player scores P1/P2
roundOver = False
ROUND_OVER_COOLDOWN = 2000

FPS = 60

#INITIATION
pygame.init()
pygame.display.set_caption("Fighter")

#SCREEN_DISPLAY
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

#load font
count_font = pygame.font.Font("graphics/Font/turok.ttf", 80)
score_font = pygame.font.Font("graphics/Font/turok.ttf", 30)

#load spritesheets
victoryImg = pygame.image.load("graphics/Font/victory.png").convert_alpha()

#FIGHTERS
Human = Fighter(1, 200, 420, False, FIGHTER_DATA, fighter_sheet, FIGHTER_ANIMATION_LIST, human_sword, sword_fx2, human_sword, sword_fx2, jump1)
Masked_Samurai = Fighter(2, 720, 420, True, MASKED_SAMURAI_DATA, masked_samurai_sheet, MASKED_SAMURAI_ANIMATION_LIST, unsheathSound, sword_fx2, unsheathSound, sword_fx2, jump2)
#FIGHTER INITIALIZATON
player1 = Human
player2 = Masked_Samurai

background = pygame.image.load("graphics/bg.jpg").convert_alpha()
backcount.play()

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
            intro_count = 4
            backcount.play()
            player1 = Human
            player2 = Masked_Samurai

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()