import pygame

def draw_background(screen, background, screen_width, screen_height):
    bg_scaled = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(bg_scaled, (0,0))