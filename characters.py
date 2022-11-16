import pygame

#SCREEN SIZE
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pygame.init()
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#CHARACTER SPRITES and DATA

fighter_sheet = pygame.image.load("graphics/fighter_sprite/fighter.png").convert_alpha()
masked_samurai_sheet = pygame.image.load("graphics\masked_samurai\masked_samurai.png").convert_alpha()
jungle_warrior_sheet = pygame.image.load("graphics\jungle_warrior\jungle_warrior.png").convert_alpha()
warrior_sheet = pygame.image.load("graphics\warrior_sprites\warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("graphics\wizard_sprites\wizard.png").convert_alpha()

#step definition
FIGHTER_ANIMATION_LIST = [8, 8, 2, 4, 4, 4, 6]
WARRIOR_ANIMATION_LIST = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_LIST = [8, 8, 1, 8, 8, 3, 7]
MASKED_SAMURAI_ANIMATION_LIST = [4, 8, 2, 4, 4, 3, 7]
JUNGLE_WARRIOR_ANIMATION_LIST = [10, 8, 3, 7, 6, 3, 11]

#HUMAN CLASS
FIGHTER_SIZE = 150
FIGHTER_SCALE = 3.8
FIGHTER_OFFSET = [60,55]
FIGHTER_DATA = [FIGHTER_SIZE, FIGHTER_SCALE, FIGHTER_OFFSET]

#WARRIOR CLASS
WARRIOR_SIZE = 162
WARRIOR_SCALE = 3.8
WARRIOR_OFFSET = [72, 60]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]

#JUNGLE CLASS
JUNGLE_WARRIOR_SIZE = 126
JUNGLE_WARRIOR_SCALE = 3
JUNGLE_WARRIOR_OFFSET = [50,30]
JUNGLE_WARRIOR_DATA = [JUNGLE_WARRIOR_SIZE, JUNGLE_WARRIOR_SCALE, JUNGLE_WARRIOR_OFFSET]

#SAMURAI CLASS
MASKED_SAMURAI_SIZE = 200
MASKED_SAMURAI_SCALE = 3.4
MASKED_SAMURAI_OFFSET = [84,82]
MASKED_SAMURAI_DATA = [MASKED_SAMURAI_SIZE, MASKED_SAMURAI_SCALE, MASKED_SAMURAI_OFFSET]

#MAGIC CLASS
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 117]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]