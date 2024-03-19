import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

white = (255, 255, 255)
red = (255, 0, 0)

circle_radius = 25
circle_x = (screen_width - circle_radius) // 2
circle_y = (screen_height - circle_radius) // 2

step = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                circle_y = max(circle_y - step, 0)
            elif event.key == pygame.K_DOWN:
                circle_y = min(circle_y + step, screen_height - circle_radius)
            elif event.key == pygame.K_LEFT:
                circle_x = max(circle_x - step, 0)
            elif event.key == pygame.K_RIGHT:
                circle_x = min(circle_x + step, screen_width - circle_radius)

    screen.fill(white)

    pygame.draw.circle(screen, red, (circle_x, circle_y), circle_radius)

    pygame.display.flip()

 
    pygame.time.Clock().tick(30)


pygame.quit()
sys.exit()
