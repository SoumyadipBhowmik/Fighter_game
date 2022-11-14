import pygame
#COLORS
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255,255,255)

def text(screen, text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img,(x,y))

#HEALTHBAR
def draw_health_bar(health, screen, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-5, y-5, 410, 40))
    pygame.draw.rect(screen, RED, (x, y, 400, 30)) #x and y is used to define where the squares will be placed
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30)) # numbers are there to determine the shape of the rectangle

#FUNCTION FOR DRAWING THE BACKGROUND
def draw_background(screen, background, screen_width, screen_height):
    bg_scaled = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(bg_scaled, (0,0))

