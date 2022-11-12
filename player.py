import pygame

class Fighter:
    def __init__(self, x, y, data, spritesheets, animation_steps):
        self.size = data[0]
        self.imageSCALED = data[1]
        self.offset = data[2]
        self.flip = False
        self.animationList = self.load_images(spritesheets, animation_steps)
        self.action = 0 #if 0 = idle, 1 = run, 2 = jump, 3 = attack 1, 4 = attack 2, 5 = hit, 6 = death
        self.frameINDEX = 0
        self.image = self.animationList[self.action][self.frameINDEX]
        self.animation_timer = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 150)) #x and y are used to place the characters in ground
        self.velocity_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, spritesheets, animation_steps):
        SPRITEBOX = self.size * self.imageSCALED
        #this function is used to extract images from the spritesheet
        animationList = []
        for y, animation in enumerate(animation_steps):
            tempImgLIST = []
            for x in range(animation):
                tempImg = spritesheets.subsurface(x * self.size, y * self.size, self.size, self.size)
                tempImgLIST.append(pygame.transform.scale(tempImg, (SPRITEBOX, SPRITEBOX)))
            animationList.append(tempImgLIST)
        return animationList

    def move(self, screen_width, screen_height, left_key, right_key, jump, screen, target):
        #VARIABLES FOR MOVEMENT
        SPEED = 10
        GRAVITY = 2
        FLOOR = screen_height - 25
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()

        if self.attacking == False:
            #KEY BINDINGS
            #jump
            if key[jump] and self.jump == False:
                self.jump = True
                self.velocity_y = -30
            #side movement
            if key[left_key]:
                dx = -SPEED
            if key[right_key]:
                dx = SPEED
            #fighter attacks
            if key[pygame.K_j] or key[pygame.K_k]:
                self.attack(screen, target)
                if key[pygame.K_j]:
                    self.attack_type = 1
                if key[pygame.K_k]:
                    self.attack_type = 2

        #apply gravity
        self.velocity_y += GRAVITY
        dy += self.velocity_y

        #ENSURING THE CHARACTER STAYS ON SCREEN
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > FLOOR:
            velocity_y = 0
            dy = FLOOR - self.rect.bottom
            self.jump = False

        #ENSURE PLAYERS ARE FACING EACH OTHER
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #MOVEMENT CONDITIONS
        self.rect.x += dx
        self.rect.y += dy

    #HANDLE ANIMATION UPDATES
    def update(self):
        animation_cooldown = 100
        self.image = self.animationList[self.action][self.frameINDEX]
        #check if the time in the current frame has passed some miliseconds
        if pygame.time.get_ticks() - self.animation_timer > animation_cooldown:
            self.frameINDEX += 1
            self.animation_timer = pygame.time.get_ticks()
        #check if the animation has finished
        if self.frameINDEX >= len(self.animationList[self.action]):
            self.frameINDEX = 0

    def attack(self, screen, target):
        attack_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)

        #COLLISION
        if attack_rect.colliderect(target.rect):
            self.attacking = True
            target.health -= 10
        pygame.draw.rect(screen, (255, 255, 100), attack_rect)

    def draw(self, screen):
        img = pygame.transform.flip(self.image, self.flip, False)
        #pygame.draw.rect(screen, (255, 100, 0), self.rect)
        screen.blit(img, (self.rect.x - (self.offset[0] * self.imageSCALED), self.rect.y - (self.offset[1] * self.imageSCALED)))