"""Block with gravity"""
import time
import pygame

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Open a window
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Gravity Simulation")

# Variables
height = screen.get_height()
width = screen.get_width()
Y_POS = 300
X_POS = 450
Y_VELOCITY = 0
X_VELOCITY = 0
new_time = time.time()

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
                if Y_VELOCITY < 5:
                    Y_VELOCITY += 3
                    if Y_VELOCITY > 5:
                        Y_VELOCITY = 5
                    new_time = time.time()

            if event.key == pygame.K_RIGHT:
                if X_VELOCITY < 5:
                    X_VELOCITY += 3
                    new_time = time.time()

            if event.key == pygame.K_LEFT:
                if X_VELOCITY > -5:
                    X_VELOCITY -= 3
                    new_time = time.time()

    # Game Logic
    if Y_POS >= 800 and Y_VELOCITY <= 0:
        Y_POS -= 1
        Y_VELOCITY = -Y_VELOCITY - 1

    elif Y_POS <= 0 and Y_VELOCITY >= 0:
        Y_POS += 1
        Y_VELOCITY = -Y_VELOCITY + 1

    if X_POS < 0 and X_VELOCITY <= 0:
        X_POS += 1
        X_VELOCITY = -X_VELOCITY

    elif X_POS > 900 and X_VELOCITY >= 0:
        X_POS -= 1
        X_VELOCITY = -X_VELOCITY

    Y_POS -= Y_VELOCITY
    X_POS += X_VELOCITY

    if time.time() - new_time >= 0.05:
        new_time = time.time()
        if Y_VELOCITY > -5:
            Y_VELOCITY -= 0.1
        if X_VELOCITY != 0:
            if X_VELOCITY > 0:
                X_VELOCITY -= 0.05
            if X_VELOCITY < 0:
                X_VELOCITY += 0.05
            if 0 < X_VELOCITY < 0.1 or -0.1 < X_VELOCITY < 0:
                X_VELOCITY = 0

    # Drawing Logic
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [0, 900, 1000, 20], 0)
    pygame.draw.rect(screen, RED, [X_POS, Y_POS, 100, 100], 0)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
