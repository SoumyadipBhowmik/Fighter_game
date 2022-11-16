import pygame
from characters import *

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.click = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                if self.click == False:
                    action = True
                    self.click = True
            else:
                self.click = False

        screen.blit(self.image,(self.rect.x, self.rect.y))
        return action



pygame.init()
#clock = pygame.time.Clock()

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# start = pygame.image.load("graphics/Menu Assets/newGame.png").convert_alpha()
# end = pygame.image.load("graphics/Menu Assets/exit.png").convert_alpha()
# game_credits = pygame.image.load("graphics/Menu Assets/credits.png").convert_alpha()

# start_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, start, 0.5)
# credits_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.45, game_credits, 0.5)
# end_button = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.15, end, 0.5)

# run = True
# while run:
#     screen.fill((5,5,5))
#     if start_button.draw():
#         print("CLICK")
#     credits_button.draw()
#     if end_button.draw():
#         run = False

#     key = pygame.key.get_pressed()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if key[pygame.K_LCTRL]:
#             if key[pygame.K_w]:
#                 run = False

#     clock.tick(60)
#     pygame.display.update()

# pygame.quit()