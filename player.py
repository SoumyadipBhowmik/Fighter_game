import pygame

class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 150)) #x and y are used to place the characters in ground
        self.velocity_y = 0
        self.jump = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, left_key, right_key, jump, screen):
        #VARIABLES FOR MOVEMENT
        SPEED = 10
        GRAVITY = 2
        FLOOR = screen_height - 25
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        #KEY BINDINGS
        #jump
        if key[jump] and self.jump == False:
            self.jump = True
            self.velocity_y = -30
        #apply gravity
        self.velocity_y += GRAVITY
        dy += self.velocity_y

        #side movement
        if key[left_key]:
            dx = -SPEED
        if key[right_key]:
            dx = SPEED

        #fighter attacks
        if key[pygame.K_j] or key[pygame.K_k]:
            self.attack(screen)
            if key[pygame.K_j]:
                self.attack_type = 1
            if key[pygame.K_k]:
                self.attack_type = 2

        #ENSURING THE CHARACTER STAYS ON SCREEN
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > FLOOR:
            velocity_y = 0
            dy = FLOOR - self.rect.bottom
            self.jump = False

        #MOVEMENT CONDITIONS
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, screen):
        attack_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(screen, (255, 255, 100), attack_rect)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 100, 0), self.rect)
