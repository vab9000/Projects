"""Snake Game"""
import time
import pygame
import snake_classes

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Open a window
size = (20*17, 20*17)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

# Variables
height = screen.get_height()
width = screen.get_width()
player = snake_classes.Snake()
berry = snake_classes.Berry(20, 20)
new_time = time.time()
ALIVE = True
WON = False
keys_pressed = list()
berry.randomize(player)
move_queue = list()

# Program Loop
CARRY_ON = True
clock = pygame.time.Clock()

while CARRY_ON:
    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CARRY_ON = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys_pressed = list()
                keys_pressed.append(pygame.K_UP)
            if event.key == pygame.K_LEFT:
                keys_pressed = list()
                keys_pressed.append(pygame.K_LEFT)
            if event.key == pygame.K_RIGHT:
                keys_pressed = list()
                keys_pressed.append(pygame.K_RIGHT)
            if event.key == pygame.K_DOWN:
                keys_pressed = list()
                keys_pressed.append(pygame.K_DOWN)
    # Drawing Logic
    screen.fill(WHITE)
    if WON:
        player.render(screen)
    elif ALIVE:
        berry.render(screen)
        player.render(screen)
        if time.time() - new_time >= 0.4:
            if pygame.K_UP in keys_pressed:
                if player.dir != 'down':
                    player.dir = 'up'
            elif pygame.K_LEFT in keys_pressed:
                if player.dir != 'right':
                    player.dir = 'left'
            elif pygame.K_RIGHT in keys_pressed:
                if player.dir != 'left':
                    player.dir = 'right'
            elif pygame.K_DOWN in keys_pressed:
                if player.dir != 'up':
                    player.dir = 'down'
            if player.check_collision():
                ALIVE = False
            player.move()
            if player.eating_berry(berry):
                berry.randomize(player)
                player.add_part()
                if len(player.parts) >= 26*26-1:
                    WON = True
            new_time = time.time()
    else:
        screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
