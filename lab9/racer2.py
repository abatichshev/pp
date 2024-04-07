import pygame
import sys
from pygame.locals import *
import random
import time

# Initialize Pygame
pygame.init()

# Set up the screen dimensions and frames per second
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Initialize game variables
SPEED = 5
SCORE = 0
COIN_THRESHOLD = 10
ENEMY_SPEED_INCREMENT = 1

# Load images and set up the display
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Set up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Define the Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, weight):
        super().__init__()
        self.weight = weight
        self.image = pygame.Surface((20, 20))  # Square representing the coin
        self.image.fill(YELLOW)  # Color the coin yellow
        self.rect = self.image.get_rect()

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Set up the sprites
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()  # Create a group for coins

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Set up a timer event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
            # Create new coins regularly
            if len(coins) < 3:  # Limit the number of coins on the screen
                coin = Coin(random.choice([1, 2, 3]))
                coin.reset_position()
                coins.add(coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background
    DISPLAYSURF.blit(background, (0, 0))

    # Render the score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Draw and move coins
    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect)
        coin.move()

    # Check collision with coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        SCORE += coin.weight

    # Increase enemy speed when the player earns N coins
    if SCORE >= COIN_THRESHOLD:
        SPEED += ENEMY_SPEED_INCREMENT
        COIN_THRESHOLD += 10

    # Check collision with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        # Handle collision with the player
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Update the display and enforce FPS
    pygame.display.update()
    FramePerSec.tick(FPS)
