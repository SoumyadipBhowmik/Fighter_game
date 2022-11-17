import pygame
from pygame import mixer
#ALL THE SOUNDS ARE KEPT IN THIS FILE
mixer.init()

#THE STARTING COUNTDOWN
backcount = pygame.mixer.Sound("sounds/321.wav")

#BACKGROUND SOUNDS
background_music = pygame.mixer.music.load("sounds/bg_music.mp3")
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.6)

#CHARACTER SOUNDS
#JUMP SOUNDS
jump1 = pygame.mixer.Sound("sounds\jump1.wav")
jump2 = pygame.mixer.Sound("sounds\jump2.wav")

#SWORD
sword_fx1 = pygame.mixer.Sound("sounds\sword_swing.mp3")
sword_fx2 = pygame.mixer.Sound("sounds\sword_swing2.wav")

unsheathSound = pygame.mixer.Sound("sounds/unsheath_sword.wav")
samurai_swordSound = pygame.mixer.Sound("sounds\samurai_sword1.wav")
human_sword = pygame.mixer.Sound("sounds\human_sword_swing.wav")

#SPECIALS
lightning_fx = pygame.mixer.Sound("sounds\lightning_strike.wav")
lightning_fx2 = pygame.mixer.Sound("sounds\lightning_strike2.wav")