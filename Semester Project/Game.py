import pygame
import random
from os import path

pygame.init()

WIDTH = 1280
HEIGHT = 760
FPS = 60

x_change = 0

#Custom Sprite
##snd_dir = path.join(path.dirname(__file__), 'images')

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#initialize pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids!")
clock = pygame.time.Clock()
##bg = pygame.image.load('./images/background.png')
pygame.mixer.music.load('gamesound.wav')
pygame.mixer.music.play(loops=0, start=0.0)

###background
##image = pygame.image.load("background.jpg").convert()
##x = 0
##
##while True:     
##
##        rel_x = x % image.get_rect().width
##        screen.blit(image, (rel_x - image.get_rect().width, 0))
##        if rel_x < WIDTH:
##            screen.blit(image, (rel_x, 0))
##        x -= 1
##
##        pygame.display.update()
##        clock.tick(FPS)

class Player(pygame.sprite.Sprite):
    
    def __init__(x,y):
        gameDisplay.blit(
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((20, 50))
##        self.image = pygame.image.load('./images/spaceship.png')
##        self.image.fill(BLUE)
##        self.rect = self.image.get_rect()
##        self.rect.centerx = WIDTH / 2
##        self.rect.bottom = HEIGHT - 300
##        self.speedx = 0
        x = (display_width * 0.45)
        y = (display_height * 0.8)
        

    def update(self):  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

            elif event.key == pygame.K_RIGHT:
                x_chnage = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

    x += x_change
    
    def shoot(self):       
        bullet = Bullet(self.rect.centerx, self.rect.top)      
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)   

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(30):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#Game loop
running = True
while running:    
    #keep loop running at the right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                
    #Update
    all_sprites.update()

    #check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = True
        print("You Lose!")

    #Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
##    screen.blit(bg,(0,0))
    #After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
