import pygame
from pygame import mixer
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
MASKED_SAMURAI_SIZE = 200
MASKED_SAMURAI_SCALE = 3.4
MASKED_SAMURAI_OFFSET = [84,82]
MASKED_SAMURAI_DATA = [MASKED_SAMURAI_SIZE, MASKED_SAMURAI_SCALE, MASKED_SAMURAI_OFFSET]

WARRIOR_SIZE = 162
WARRIOR_SCALE = 3.8
WARRIOR_OFFSET = [72, 60]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 117]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

intro_count = 4
countUpdate = pygame.time.get_ticks()


score = [0, 0] #player scores P1/P2
roundOver = False
ROUND_OVER_COOLDOWN = 2000

FPS = 60

#INITIATION
mixer.init()
pygame.init()
pygame.display.set_caption("Fighter")

#step definition
WARRIOR_ANIMATION_LIST = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_LIST = [8, 8, 1, 8, 8, 3, 7]
MASKED_SAMURAI_ANIMATION_LIST = [4, 8, 2, 4, 4, 3, 7]

#SCREEN_DISPLAY
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

#load font
count_font = pygame.font.Font("graphics/Font/turok.ttf", 80)
score_font = pygame.font.Font("graphics/Font/turok.ttf", 30)

#sounds
backcount = pygame.mixer.Sound("sounds/321.wav")
#background_music = pygame.mixer.music.load("sounds/bg_music.mp3")
sword_fx1 = pygame.mixer.Sound("sounds\sword_swing.mp3")
sword_fx2 = pygame.mixer.Sound("sounds\sword_swing2.wav")
lightning_fx = pygame.mixer.Sound("sounds\lightning_strike.wav")
lightning_fx2 = pygame.mixer.Sound("sounds\lightning_strike2.wav")
#pygame.mixer.music.play(-1, 0.0, 5000)


#load spritesheets
masked_samurai_sheet = pygame.image.load("graphics\masked_samurai\masked_samurai.png").convert_alpha()
warrior_sheet = pygame.image.load("graphics\warrior_sprites\warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("graphics\wizard_sprites\wizard.png").convert_alpha()
victoryImg = pygame.image.load("graphics/Font/victory.png").convert_alpha()

#FIGHTERS
player1 = Fighter(1, 200, 420, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_LIST, sword_fx1, sword_fx2, lightning_fx, lightning_fx2)
player2 = Fighter(2, 720, 420, True, MASKED_SAMURAI_DATA, masked_samurai_sheet, MASKED_SAMURAI_ANIMATION_LIST, sword_fx1, sword_fx2, lightning_fx, lightning_fx2)


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
            player1 = Fighter(1, 200, 420, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_LIST, sword_fx1, sword_fx2, lightning_fx, lightning_fx2)
            player2 = Fighter(2, 700, 420, True, MASKED_SAMURAI_DATA, masked_samurai_sheet, MASKED_SAMURAI_ANIMATION_LIST, sword_fx1, sword_fx2, lightning_fx, lightning_fx2)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()