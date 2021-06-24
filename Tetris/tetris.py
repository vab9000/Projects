import random
import pygame
import time

pygame.init()
pygame.font.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 127, 0)
GRAY = (127, 127, 127)

# Open a window
size = (450, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

# Variables
height = screen.get_height()
width = screen.get_width()
BLOCK_PLACED = True
X_BLOCK_POS = 120
Y_BLOCK_POS = 0
BLOCK_ROT = 0
PLACE_BLOCK = None
myfont = pygame.font.SysFont('Arial', 30)
new_time = time.time()
new_time2 = time.time()
new_time3 = time.time()
placed_blocks = list()
grid = list()
queue = list()
SCORE = 0
SPEED = 0.5
queue.append(random.randint(1, 7))
queue.append(random.randint(1, 7))
queue.append(random.randint(1, 7))
i = 0
while i < 16:
    column = list()
    j = 0
    while j < 41:
        column.append(False)
        j += 1
    grid.append(column)
    i += 1
color_grid = list()
i = 0
while i < 16:
    column = list()
    j = 0
    while j < 41:
        column.append(WHITE)
        j += 1
    color_grid.append(column)
    i += 1

# Blocks


def o_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if falling_block:
        if (
            grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20 + 1)] or grid[int(xPos/20) + 1][int(yPos/20) + 2]
        ):
            BLOCK_PLACED = True
            color_grid[int(xPos/20)][int(yPos/20)] = YELLOW
            color_grid[int(xPos/20)][int(yPos/20) + 1] = YELLOW
            color_grid[int(xPos/20) + 1][int(yPos/20)] = YELLOW
            color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = YELLOW
            grid[int(xPos/20)][int(yPos/20)] = True
            grid[int(xPos/20)][int(yPos/20) + 1] = True
            grid[int(xPos/20) + 1][int(yPos/20)] = True
            grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
    pygame.draw.rect(screen, YELLOW, [xPos, yPos, 20, 20], 0)
    pygame.draw.rect(screen, YELLOW, [xPos + 20, yPos, 20, 20], 0)
    pygame.draw.rect(screen, YELLOW, [xPos, yPos + 20, 20, 20], 0)
    pygame.draw.rect(screen, YELLOW, [xPos + 20, yPos + 20, 20, 20], 0)
def i_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if rot == 0 or rot == 180:
        if falling_block:
            if (grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 3] or grid[int(xPos/20)][int(yPos/20) + 4]):
                BLOCK_PLACED = True
                color_grid[int(xPos/20)][int(yPos/20)] = CYAN
                color_grid[int(xPos/20)][int(yPos/20) + 1] = CYAN
                color_grid[int(xPos/20)][int(yPos/20) + 2] = CYAN
                color_grid[int(xPos/20)][int(yPos/20) + 3] = CYAN
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20)][int(yPos/20) + 2] = True
                grid[int(xPos/20)][int(yPos/20) + 3] = True
        pygame.draw.rect(screen, CYAN, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, CYAN, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, CYAN, [xPos, yPos + 40, 20, 20], 0)
        pygame.draw.rect(screen, CYAN, [xPos, yPos + 60, 20, 20], 0)
    elif rot == 90 or rot == 270:
        if falling_block:
            if (grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20) + 1]):
                BLOCK_PLACED = True
                color_grid[int(xPos/20)][int(yPos/20)] = CYAN
                color_grid[int(xPos/20) + 1][int(yPos/20)] = CYAN
                color_grid[int(xPos/20) + 2][int(yPos/20)] = CYAN
                color_grid[int(xPos/20) + 3][int(yPos/20)] = CYAN
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 2][int(yPos/20)] = True
                grid[int(xPos/20) + 3][int(yPos/20)] = True
        pygame.draw.rect(screen, CYAN, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, CYAN, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, CYAN, [xPos + 40, yPos, 20, 20], 0)
        pygame.draw.rect(screen, CYAN, [xPos + 60, yPos, 20, 20], 0)
def t_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if rot == 0:
        if falling_block:
            if (grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 3] or grid[int(xPos/20) + 1][int(yPos/20) + 2]):
                BLOCK_PLACED = True
                color_grid[int(xPos/20)][int(yPos/20)] = PURPLE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = PURPLE
                color_grid[int(xPos/20)][int(yPos/20) + 2] = PURPLE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = PURPLE
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20)][int(yPos/20) + 2] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
        pygame.draw.rect(screen, PURPLE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos, yPos + 40, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos + 20, 20, 20], 0)
    elif rot == 90:
        if falling_block:
            if (grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2]):
                BLOCK_PLACED = True
                color_grid[int(xPos/20)][int(yPos/20)] = PURPLE
                color_grid[int(xPos/20) + 1][int(yPos/20)] = PURPLE
                color_grid[int(xPos/20) + 2][int(yPos/20)] = PURPLE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = PURPLE
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 2][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
        pygame.draw.rect(screen, PURPLE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 40, yPos, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos + 20, 20, 20], 0)
    elif rot == 180:
        if falling_block:
            if (grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 3]):
                BLOCK_PLACED = True
                color_grid[int(xPos/20) + 1][int(yPos/20)] = PURPLE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = PURPLE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = PURPLE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 2] = PURPLE
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 2] = True
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos + 40, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos, yPos + 20, 20, 20], 0)
    elif rot == 270:
        if falling_block:
            if (grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 2][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2]):
                BLOCK_PLACED = True
                color_grid[int(xPos/20) + 1][int(yPos/20)] = PURPLE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = PURPLE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = PURPLE
                color_grid[int(xPos/20) + 2][int(yPos/20) + 1] = PURPLE
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 2][int(yPos/20) + 1] = True
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, PURPLE, [xPos + 40, yPos + 20, 20, 20], 0)
def s_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if rot == 0 or rot == 180:
        if falling_block:
            if (grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2]):
                BLOCK_PLACED = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 2][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                color_grid[int(xPos/20) + 1][int(yPos/20)] = GREEN
                color_grid[int(xPos/20) + 2][int(yPos/20)] = GREEN
                color_grid[int(xPos/20)][int(yPos/20) + 1] = GREEN
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = GREEN
        pygame.draw.rect(screen, GREEN, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, GREEN, [xPos + 40, yPos, 20, 20], 0)
        pygame.draw.rect(screen, GREEN, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, GREEN, [xPos + 20, yPos + 20, 20, 20], 0)
    elif rot == 90 or rot == 270:
        if falling_block:
            if (grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 3]):
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 2] = True
                color_grid[int(xPos/20)][int(yPos/20)] = GREEN
                color_grid[int(xPos/20)][int(yPos/20) + 1] = GREEN
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = GREEN
                color_grid[int(xPos/20) + 1][int(yPos/20) + 2] = GREEN
        pygame.draw.rect(screen, GREEN, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, GREEN, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, GREEN, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, GREEN, [xPos + 20, yPos + 40, 20, 20], 0)
def z_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if rot == 0 or rot == 180:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 2][int(yPos/20) + 1] = True
                color_grid[int(xPos/20)][int(yPos/20)] = RED
                color_grid[int(xPos/20) + 1][int(yPos/20)] = RED
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = RED
                color_grid[int(xPos/20) + 2][int(yPos/20) + 1] = RED
        pygame.draw.rect(screen, RED, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, RED, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, RED, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, RED, [xPos + 40, yPos + 20, 20, 20], 0)
    elif rot == 90 or rot == 270:
        if falling_block:
            if grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 3]:
                BLOCK_PLACED = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20)][int(yPos/20) + 2] = True
                color_grid[int(xPos/20) + 1][int(yPos/20)] = RED
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = RED
                color_grid[int(xPos/20)][int(yPos/20) + 1] = RED
                color_grid[int(xPos/20)][int(yPos/20) + 2] = RED
        pygame.draw.rect(screen, RED, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, RED, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, RED, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, RED, [xPos, yPos + 40, 20, 20], 0)
def j_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if rot == 0:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 2][int(yPos/20) + 1] = True
                color_grid[int(xPos/20)][int(yPos/20)] = BLUE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = BLUE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = BLUE
                color_grid[int(xPos/20) + 2][int(yPos/20) + 1] = BLUE
        pygame.draw.rect(screen, BLUE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 40, yPos + 20, 20, 20], 0)
    elif rot == 90:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 3]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20)][int(yPos/20) + 2] = True
                color_grid[int(xPos/20)][int(yPos/20)] = BLUE
                color_grid[int(xPos/20) + 1][int(yPos/20)] = BLUE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = BLUE
                color_grid[int(xPos/20)][int(yPos/20) + 2] = BLUE
        pygame.draw.rect(screen, BLUE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos, yPos + 40, 20, 20], 0)
    elif rot == 180:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 2][int(yPos/20)] = True
                grid[int(xPos/20) + 2][int(yPos/20) + 1] = True
                color_grid[int(xPos/20)][int(yPos/20)] = BLUE
                color_grid[int(xPos/20) + 1][int(yPos/20)] = BLUE
                color_grid[int(xPos/20) + 2][int(yPos/20)] = BLUE
                color_grid[int(xPos/20) + 2][int(yPos/20) + 1] = BLUE
        pygame.draw.rect(screen, BLUE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 40, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 40, yPos + 20, 20, 20], 0)
    elif rot == 270:
        if falling_block:
            if grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 3] or grid[int(xPos/20)][int(yPos/20) + 3]:
                BLOCK_PLACED = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 2] = True
                grid[int(xPos/20)][int(yPos/20) + 2] = True
                color_grid[int(xPos/20) + 1][int(yPos/20)] = BLUE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = BLUE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 2] = BLUE
                color_grid[int(xPos/20)][int(yPos/20) + 2] = BLUE
        pygame.draw.rect(screen, BLUE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos + 20, yPos + 40, 20, 20], 0)
        pygame.draw.rect(screen, BLUE, [xPos, yPos + 40, 20, 20], 0)
def l_block(xPos, yPos, rot, falling_block):
    global BLOCK_PLACED
    if rot == 0:
        if falling_block:
            if grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                BLOCK_PLACED = True
                grid[int(xPos/20) + 2][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 2][int(yPos/20) + 1] = True
                color_grid[int(xPos/20) + 2][int(yPos/20)] = ORANGE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = ORANGE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = ORANGE
                color_grid[int(xPos/20) + 2][int(yPos/20) + 1] = ORANGE
        pygame.draw.rect(screen, ORANGE, [xPos + 40, yPos, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 40, yPos + 20, 20, 20], 0)
    elif rot == 90:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 3] or grid[int(xPos/20) + 1][int(yPos/20) + 3]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20)][int(yPos/20) + 2] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 2] = True
                color_grid[int(xPos/20)][int(yPos/20)] = ORANGE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = ORANGE
                color_grid[int(xPos/20)][int(yPos/20) + 2] = ORANGE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 2] = ORANGE
        pygame.draw.rect(screen, ORANGE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos, yPos + 40, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 20, yPos + 40, 20, 20], 0)
    elif rot == 180:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20)][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 2][int(yPos/20)] = True
                color_grid[int(xPos/20)][int(yPos/20)] = ORANGE
                color_grid[int(xPos/20)][int(yPos/20) + 1] = ORANGE
                color_grid[int(xPos/20) + 1][int(yPos/20)] = ORANGE
                color_grid[int(xPos/20) + 2][int(yPos/20)] = ORANGE
        pygame.draw.rect(screen, ORANGE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 40, yPos, 20, 20], 0)
    elif rot == 270:
        if falling_block:
            if grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 3]:
                BLOCK_PLACED = True
                grid[int(xPos/20)][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20)] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 1] = True
                grid[int(xPos/20) + 1][int(yPos/20) + 2] = True
                color_grid[int(xPos/20)][int(yPos/20)] = ORANGE
                color_grid[int(xPos/20) + 1][int(yPos/20)] = ORANGE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 1] = ORANGE
                color_grid[int(xPos/20) + 1][int(yPos/20) + 2] = ORANGE
        pygame.draw.rect(screen, ORANGE, [xPos, yPos, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 20, yPos, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 20, yPos + 20, 20, 20], 0)
        pygame.draw.rect(screen, ORANGE, [xPos + 20, yPos + 40, 20, 20], 0)

def draw_squares():
    global SCORE
    global SPEED
    i = 0
    while i < 40:
        j = 0
        while j < 15:
            if grid[j][i] == False:
                break
            j += 1
        if j == 15:
            SCORE += 100
            SPEED -= 0.01
            k = 0
            while k < 15:
                grid[k].pop(i)
                grid[k].insert(0, False)
                color_grid[k].pop(i)
                color_grid[k].insert(0, WHITE)
                k += 1
        i += 1
    i = 0
    for column in color_grid:
        j = 0
        for square in column:
            if square != WHITE:
                pygame.draw.rect(screen, square, (i*20, j*20, 20, 20), 0)
            if i < 15:
                pygame.draw.rect(screen, GRAY, (i*20, j*20, 2, 20), 0)
                pygame.draw.rect(screen, GRAY, (i*20, j*20, 20, 2), 0)
                pygame.draw.rect(screen, GRAY, (i*20, j*20 + 18, 2, 20), 0)
                pygame.draw.rect(screen, GRAY, (i*20 + 18, j*20, 20, 2), 0)
            j += 1
        i += 1

def side_collisions(blockType, xPos, yPos, rot, dir):
    if dir == 'left':
        if blockType == 1:
            if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20 + 1)] or grid[int(xPos/20)][int(yPos/20) + 1]:
                return False
        elif blockType == 2:
            if rot == 0 or rot == 180:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 2] or grid[int(xPos/20) - 1][int(yPos/20) + 3]:
                    return False
            if rot == 90 or rot == 270:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)]:
                    return False
        elif blockType == 3:
            if rot == 0:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 1]:
                    return False
            elif rot == 90:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20)]:
                    return False
            elif rot == 180:
                if grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2]:
                    return False
            elif rot  == 270:
                if grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20)  + 1] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1]:
                    return False
        elif blockType == 4:
            if rot == 0 or rot == 180:
                if grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20)]:
                    return False
            if rot == 90 or rot == 270:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2]:
                    return False
        elif blockType == 5:
            if rot == 0 or rot == 180:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1]:
                    return False
            if rot == 90 or rot == 270:
                if grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 2]:
                    return False
        elif blockType == 6:
            if rot == 0:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1]:
                    return False
            elif rot == 90:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 2]:
                    return False
            elif rot == 180:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1]:
                    return False
            elif rot == 270:
                if grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) - 1][int(yPos/20) + 2]:
                    return False
        elif blockType == 7:
            if rot == 0:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1]:
                    return False
            elif rot == 90:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20) - 1][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 2]:
                    return False
            elif rot == 180:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20) - 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)]:
                    return False
            elif rot == 270:
                if grid[int(xPos/20) - 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2]:
                    return False
    elif dir == 'right':
        if blockType == 1:
            if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20 + 1)] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                return False
        elif blockType == 2:
            if rot == 0 or rot == 180:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 3]:
                    return False
            if rot == 90 or rot == 270:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 3][int(yPos/20)] or grid[int(xPos/20) + 4][int(yPos/20)]:
                    return False
        elif blockType == 3:
            if rot == 0:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                    return False
            elif rot == 90:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20)]:
                    return False
            elif rot == 180:
                if grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                    return False
            elif rot  == 270:
                if grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)  + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20) + 1]:
                    return False
        elif blockType == 4:
            if rot == 0 or rot == 180:
                if grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20)]:
                    return False
            if rot == 90 or rot == 270:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                    return False
        elif blockType == 5:
            if rot == 0 or rot == 180:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20) + 1]:
                    return False
            if rot == 90 or rot == 270:
                if grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                    return False
        elif blockType == 6:
            if rot == 0:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20) + 1]:
                    return False
            elif rot == 90:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                    return False
            elif rot == 180:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 3][int(yPos/20)] or grid[int(xPos/20) + 3][int(yPos/20) + 1]:
                    return False
            elif rot == 270:
                if grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                    return False
        elif blockType == 7:
            if rot == 0:
                if grid[int(xPos/20) + 3][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 3][int(yPos/20) + 1]:
                    return False
            elif rot == 90:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                    return False
            elif rot == 180:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 3][int(yPos/20)]:
                    return False
            elif rot == 270:
                if grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 2]:
                    return False
    return True

def rot_collisions(blockType, xPos, yPos, rot):
    global BLOCK_ROT
    if blockType == 2:
        if rot == 0 or rot == 180:
            if int(yPos/20) > 36:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 3]:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
        elif rot == 90 or rot == 270:
            if int(xPos/20) > 11:
                if rot == 270:
                    BLOCK_ROT = 180
                if rot == 90:
                    BLOCK_ROT = 0
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 3][int(yPos/20)]:
                if rot == 270:
                    BLOCK_ROT = 180
                if rot == 90:
                    BLOCK_ROT = 0
    elif blockType == 3:
        if rot == 0:
            if int(yPos/20) > 37:
                BLOCK_ROT = 270
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2]:
                BLOCK_ROT = 270
        elif rot == 90:
            if int(xPos/20) > 12:
                BLOCK_ROT = 0
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20)]:
                BLOCK_ROT = 0
        elif rot == 180:
            if int(yPos/20) > 37:
                BLOCK_ROT = 90
            elif grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                BLOCK_ROT = 90
        elif rot == 270:
            if int(xPos/20) > 12:
                BLOCK_ROT = 180
            elif grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                BLOCK_ROT = 180
    elif blockType == 4:
        if rot == 0 or rot == 180:
            if int(xPos/20) > 12:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
            elif grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20)]:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
        elif rot == 90 or rot == 270:
            if int(yPos/20) > 37:
                if rot == 90:
                    BLOCK_ROT = 0
                elif rot == 270:
                    BLOCK_ROT = 180
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                if rot == 90:
                    BLOCK_ROT = 0
                elif rot == 270:
                    BLOCK_ROT = 180
    elif blockType == 5:
        if rot == 0 or rot == 180:
            if int(xPos/20) > 12:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
        elif rot == 90 or rot == 270:
            if int(yPos/20) > 37:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
            elif grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2]:
                if rot == 0:
                    BLOCK_ROT = 270
                if rot == 180:
                    BLOCK_ROT = 90
    elif blockType == 6:
        if rot == 0:
            if int(xPos/20) > 12:
                BLOCK_ROT = 270
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                BLOCK_ROT = 270
        elif rot == 90:
            if int(yPos/20) > 37:
                BLOCK_ROT = 0
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2]:
                BLOCK_ROT = 0
        elif rot == 180:
            if int(xPos/20) > 12:
                BLOCK_ROT = 90
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                BLOCK_ROT = 90
        elif rot == 270:
            if int(yPos/20) > 37:
                BLOCK_ROT = 180
            elif grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2] or grid[int(xPos/20)][int(yPos/20) + 2]:
                BLOCK_ROT = 180
    elif blockType == 7:
        if rot == 0:
            if int(xPos/20) > 12:
                BLOCK_ROT = 270
            elif grid[int(xPos/20) + 2][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 2][int(yPos/20) + 1]:
                BLOCK_ROT = 270
        elif rot == 90:
            if int(yPos/20) > 37:
                BLOCK_ROT = 0
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20)][int(yPos/20) + 2] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                BLOCK_ROT = 0
        elif rot == 180:
            if int(xPos/20) > 12:
                BLOCK_ROT = 90
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20)][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 2][int(yPos/20)]:
                BLOCK_ROT = 90
        elif rot == 270:
            if int(yPos/20) > 37:
                BLOCK_ROT = 180
            elif grid[int(xPos/20)][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20)] or grid[int(xPos/20) + 1][int(yPos/20) + 1] or grid[int(xPos/20) + 1][int(yPos/20) + 2]:
                BLOCK_ROT = 180

# Program Loop
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    # Main Event Loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                BLOCK_ROT += 90
                if BLOCK_ROT == 360:
                    BLOCK_ROT = 0
                rot_collisions(PLACE_BLOCK, X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT)
            elif event.key == pygame.K_LEFT:
                if side_collisions(PLACE_BLOCK, X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, 'left'):
                    X_BLOCK_POS -= 20
                if X_BLOCK_POS < 0:
                    X_BLOCK_POS = 0
            elif event.key == pygame.K_RIGHT:
                if side_collisions(PLACE_BLOCK, X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, 'right'):
                    X_BLOCK_POS += 20
            elif event.key == pygame.K_DOWN:
                SPEED /= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                SPEED *= 5
            
    # Game Logic
    if (PLACE_BLOCK == 1 or (PLACE_BLOCK == 3 and (BLOCK_ROT == 0 or BLOCK_ROT == 180)) or ((PLACE_BLOCK == 4 or PLACE_BLOCK == 5) and (BLOCK_ROT == 90 or BLOCK_ROT == 270)) or ((PLACE_BLOCK == 6 or PLACE_BLOCK == 7) and (BLOCK_ROT == 90 or BLOCK_ROT == 270))) and X_BLOCK_POS > 260:
        X_BLOCK_POS = 260
    elif PLACE_BLOCK == 2 and (BLOCK_ROT == 0 or BLOCK_ROT == 180) and X_BLOCK_POS > 280:
        X_BLOCK_POS = 280
    elif PLACE_BLOCK == 2 and (BLOCK_ROT == 90 or BLOCK_ROT == 270) and X_BLOCK_POS > 220:
        X_BLOCK_POS = 220
    elif ((PLACE_BLOCK == 3 and (BLOCK_ROT == 90 or BLOCK_ROT == 270)) or ((PLACE_BLOCK == 4 or PLACE_BLOCK == 5) and (BLOCK_ROT == 0 or BLOCK_ROT == 180)) or ((PLACE_BLOCK == 6 or PLACE_BLOCK == 7) and (BLOCK_ROT == 0 or BLOCK_ROT == 180))) and X_BLOCK_POS > 240:
        X_BLOCK_POS = 240
    if new_time2 >= SPEED * 2:
        if BLOCK_PLACED == False:
            if (PLACE_BLOCK == 1 or (PLACE_BLOCK == 3 and (BLOCK_ROT == 90 or BLOCK_ROT == 270)) or ((PLACE_BLOCK == 4 or PLACE_BLOCK == 5) and (BLOCK_ROT == 0 or BLOCK_ROT == 180)) or ((PLACE_BLOCK == 6 or PLACE_BLOCK == 7) and (BLOCK_ROT == 0 or BLOCK_ROT == 180))) and Y_BLOCK_POS > 760:
                Y_BLOCK_POS = 760
                if PLACE_BLOCK == 1:
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = YELLOW
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = YELLOW
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = YELLOW
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = YELLOW
                elif PLACE_BLOCK == 3:
                    if BLOCK_ROT == 90:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = PURPLE
                    elif BLOCK_ROT == 270:
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = True
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = PURPLE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = PURPLE
                elif PLACE_BLOCK == 4:
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = GREEN
                    color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = GREEN
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = GREEN
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = GREEN
                elif PLACE_BLOCK == 5:
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = True
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = RED
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = RED
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = RED
                    color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = RED
                elif PLACE_BLOCK == 6:
                    if BLOCK_ROT == 0:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = BLUE
                    elif BLOCK_ROT == 180:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = BLUE
                elif PLACE_BLOCK == 7:
                    if BLOCK_ROT == 0:
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = True
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = ORANGE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20) + 1] = ORANGE
                    elif BLOCK_ROT == 180:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = ORANGE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = ORANGE
                BLOCK_PLACED = True
                X_BLOCK_POS = 120
                Y_BLOCK_POS = 0
            elif PLACE_BLOCK == 2 and (BLOCK_ROT == 90 or BLOCK_ROT == 270) and Y_BLOCK_POS > 780:
                Y_BLOCK_POS = 780
                grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = True
                grid[int(X_BLOCK_POS/20) + 3][int(Y_BLOCK_POS/20)] = True
                color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = CYAN
                color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = CYAN
                color_grid[int(X_BLOCK_POS/20) + 2][int(Y_BLOCK_POS/20)] = CYAN
                color_grid[int(X_BLOCK_POS/20) + 3][int(Y_BLOCK_POS/20)] = CYAN
                BLOCK_PLACED = True
                X_BLOCK_POS = 120
                Y_BLOCK_POS = 0
            elif PLACE_BLOCK == 2 and (BLOCK_ROT == 0 or BLOCK_ROT == 180) and Y_BLOCK_POS > 720:
                Y_BLOCK_POS = 720
                grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = True
                grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 3] = True
                color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = CYAN
                color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = CYAN
                color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = CYAN
                color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 3] = CYAN
                BLOCK_PLACED = True
                X_BLOCK_POS = 120
                Y_BLOCK_POS = 0
            elif ((PLACE_BLOCK == 3 and (BLOCK_ROT == 0 or BLOCK_ROT == 180)) or ((PLACE_BLOCK == 4 or PLACE_BLOCK == 5) and (BLOCK_ROT == 90 or BLOCK_ROT == 270)) or ((PLACE_BLOCK == 6 or PLACE_BLOCK == 7) and (BLOCK_ROT == 90 or BLOCK_ROT == 270))) and Y_BLOCK_POS > 740:
                Y_BLOCK_POS = 740
                if PLACE_BLOCK == 3:
                    if BLOCK_ROT == 0:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = PURPLE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = PURPLE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = PURPLE
                    elif BLOCK_ROT == 180:
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = True
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = PURPLE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = PURPLE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = PURPLE
                elif PLACE_BLOCK == 4:
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = True
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = GREEN
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = GREEN
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = GREEN
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = GREEN
                elif PLACE_BLOCK == 5:
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                    grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                    grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = True
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = RED
                    color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = RED
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = RED
                    color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = RED
                elif PLACE_BLOCK == 6:
                    if BLOCK_ROT == 90:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = BLUE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = BLUE
                    elif BLOCK_ROT == 270:
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = True
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = BLUE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = BLUE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = BLUE
                elif PLACE_BLOCK == 7:
                    if BLOCK_ROT == 90:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = ORANGE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 1] = ORANGE
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20) + 2] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = ORANGE
                    elif BLOCK_ROT == 270:
                        grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = True
                        grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = True
                        color_grid[int(X_BLOCK_POS/20)][int(Y_BLOCK_POS/20)] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20)] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 1] = ORANGE
                        color_grid[int(X_BLOCK_POS/20) + 1][int(Y_BLOCK_POS/20) + 2] = ORANGE
                BLOCK_PLACED = True
                X_BLOCK_POS = 120
                Y_BLOCK_POS = 0
        new_time2 = time.time()
        
    # Drawing Logic
    screen.fill(BLACK)
    
    if BLOCK_PLACED:
        X_BLOCK_POS = 120
        Y_BLOCK_POS = 0
        BLOCK_ROT = 0
        queue.append(random.randint(1, 7))
        PLACE_BLOCK = queue[0]
        queue.pop(0)
        BLOCK_PLACED = False
    if time.time() - new_time3 >= SPEED:
        if PLACE_BLOCK == 1:
            o_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        elif PLACE_BLOCK == 2:
            i_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        elif PLACE_BLOCK == 3:
            t_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        elif PLACE_BLOCK == 4:
            s_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        elif PLACE_BLOCK == 5:
            z_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        elif PLACE_BLOCK == 6:
            j_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        elif PLACE_BLOCK == 7:
            l_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, True)
        new_time3 = time.time()
    elif time.time() - new_time3 < SPEED:
        if PLACE_BLOCK == 1:
            o_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
        elif PLACE_BLOCK == 2:
            i_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
        elif PLACE_BLOCK == 3:
            t_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
        elif PLACE_BLOCK == 4:
            s_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
        elif PLACE_BLOCK == 5:
            z_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
        elif PLACE_BLOCK == 6:
            j_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
        elif PLACE_BLOCK == 7:
            l_block(X_BLOCK_POS, Y_BLOCK_POS, BLOCK_ROT, False)
    if queue[0] == 1:
        o_block(350, 200, 0, False)
    elif queue[0] == 2:
        i_block(350, 200, 0, False)
    elif queue[0] == 3:
        t_block(350, 200, 0, False)
    elif queue[0] == 4:
        s_block(350, 200, 0, False)
    elif queue[0] == 5:
        z_block(350, 200, 0, False)
    elif queue[0] == 6:
        j_block(350, 200, 0, False)
    elif queue[0] == 7:
        l_block(350, 200, 0, False)
    if queue[1] == 1:
        o_block(350, 400, 0, False)
    elif queue[1] == 2:
        i_block(350, 400, 0, False)
    elif queue[1] == 3:
        t_block(350, 400, 0, False)
    elif queue[1] == 4:
        s_block(350, 400, 0, False)
    elif queue[1] == 5:
        z_block(350, 400, 0, False)
    elif queue[1] == 6:
        j_block(350, 400, 0, False)
    elif queue[1] == 7:
        l_block(350, 400, 0, False)
    if queue[2] == 1:
        o_block(350, 600, 0, False)
    elif queue[2] == 2:
        i_block(350, 600, 0, False)
    elif queue[2] == 3:
        t_block(350, 600, 0, False)
    elif queue[2] == 4:
        s_block(350, 600, 0, False)
    elif queue[2] == 5:
        z_block(350, 600, 0, False)
    elif queue[2] == 6:
        j_block(350, 600, 0, False)
    elif queue[2] == 7:
        l_block(350, 600, 0, False)
    textsurface = myfont.render('Queue', False, (255, 255, 255))
    screen.blit(textsurface,(340, 50))
    pygame.draw.rect(screen, GRAY, (300, 0, 20, 800), 0)
    textsurface = myfont.render('Score:', False, (255, 255, 255))
    screen.blit(textsurface,(330, 700))
    textsurface = myfont.render(str(SCORE), False, (255, 255, 255))
    screen.blit(textsurface,(330, 730))
    pygame.draw.rect(screen, GRAY, (300, 0, 20, 800), 0)
    if time.time() - new_time >= SPEED:
        if BLOCK_PLACED == False:
            Y_BLOCK_POS += 20
        new_time = time.time()
    
    draw_squares()
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()