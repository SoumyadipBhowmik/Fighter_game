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

start = pygame.image.load("graphics/Menu Assets/newGame.png").convert_alpha()
end = pygame.image.load("graphics/Menu Assets/exit.png").convert_alpha()
game_credits = pygame.image.load("graphics/Menu Assets/credits.png").convert_alpha()
