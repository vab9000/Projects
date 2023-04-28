# Minesweeper
from numpy import ndarray, zeros
from random import randrange
from pygame import K_SPACE, KEYUP, MOUSEBUTTONDOWN, K_v, init, quit, time, display, event, QUIT, draw, mouse, font, KEYDOWN

# initialize pygame
init()

# define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (122, 122, 122)

# define constants
GRID_DIM = (10, 10)
CELL_SIZE = 50

# global variables
won = 0
uncovered = 0
total_empty = 0
flags = 0
reveal_map = False

# setup pygame
size = (GRID_DIM[0]*CELL_SIZE, GRID_DIM[1]*CELL_SIZE + 100)
screen = display.set_mode(size)
display.set_caption("MINESWEEPER")
height = screen.get_height()
width = screen.get_width()
carry_on = True
clock = time.Clock()
color = GREY
mouse_pos = mouse.get_pos()
myfont = font.SysFont('Courier New', 30)

def generate_grid(grid: ndarray) -> None:
    global total_empty, flags
    def get_adjacent_bombs(i: int, j: int) -> int:
        adjacents = get_adjacents(i, j)
        total = 0
        for val in adjacents:
            if grid[val[0], val[1]] == "nb":
                total += 1
        return total

    rand = randrange(0, 16)
    for i in range(GRID_DIM[0]):
        for j in range(GRID_DIM[1]):
            if rand < 12:
                grid[i, j] = "n"
                total_empty += 1
            else:
                grid[i, j] = "nb"
                flags += 1
            rand = randrange(0, 16)

    for i in range(GRID_DIM[0]):
        for j in range(GRID_DIM[1]):
            if grid[i, j] == "n":
                grid[i, j] = "n" + str(get_adjacent_bombs(i, j))

def get_adjacents(i: int, j: int) -> list:
        adjacents = []
        if i < GRID_DIM[0] - 1:
            adjacents.append((i + 1, j))
            if j < GRID_DIM[1] - 1:
                adjacents.append((i + 1, j + 1))
            if j > 0:
                adjacents.append((i + 1, j - 1))
        if i > 0:
            adjacents.append((i - 1, j))
            if j < GRID_DIM[1] - 1:
                adjacents.append((i - 1, j + 1))
            if j > 0:
                adjacents.append((i - 1, j - 1))
        if j < GRID_DIM[1] - 1:
            adjacents.append((i, j + 1))
        if j > 0:
            adjacents.append((i, j - 1))
        return adjacents


def reset() -> None:
    global won, uncovered, total_empty, flags
    won = 0
    uncovered = 0
    total_empty = 0
    flags = 0
    generate_grid(grid)
    zero_cells = get_zeros()
    rand_zero = zero_cells[randrange(0, len(zero_cells))]
    grid[rand_zero[0], rand_zero[1]] = "r" + grid[rand_zero[0], rand_zero[1]][1]
    clear_adjacents(rand_zero[0], rand_zero[1])

def clear_adjacents(i, j) -> None:
    global uncovered
    if grid[i, j] == "r0":
        adjacents = get_adjacents(i, j)
        for x in adjacents:
            if grid[x[0], x[1]][1] != "b" and grid[x[0], x[1]][0] == "n":
                grid[x[0], x[1]] = "r" + grid[x[0], x[1]][1]
                uncovered += 1
                clear_adjacents(x[0], x[1])

def get_zeros() -> list:
    cells = []
    for i in range(GRID_DIM[0]):
        for j in range(GRID_DIM[1]):
            if grid[i, j] == "n0":
                cells.append((i, j))
    
    return cells

# 0 - 8 = # of bombs adjacent
# starting with n = not revealed
# starting with r = revealed
# b = bomb
# nb = unrevealed bomb
# create the grid
grid = zeros((GRID_DIM[0], GRID_DIM[1]), dtype='<U2')
generate_grid(grid)
zero_cells = get_zeros()
rand_zero = zero_cells[randrange(0, len(zero_cells))]
grid[rand_zero[0], rand_zero[1]] = "r" + grid[rand_zero[0], rand_zero[1]][1]
clear_adjacents(rand_zero[0], rand_zero[1])

while carry_on:
    # Main Event Loop

    for evt in event.get():
        if evt.type == QUIT:
            carry_on = False
        
        if evt.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            if mouse_pos[1] > height - 100:
                continue
            if evt.button == 1:
                if grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][0] == "n":
                    grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE] = "r" + grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][1]
                    if grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][1] == "b":
                        won = -1
                    if grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][1] == "0":
                        clear_adjacents(mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE)
                    uncovered += 1
                    if total_empty - 1 == uncovered:
                        won = 1

            elif evt.button == 3:
                if grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][0] == "n":
                    if flags > 0:
                        grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE] = "f" + grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][1]
                        flags -= 1
                elif grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][0] == "f":
                    flags += 1
                    grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE] = "n" + grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE][1]

        if evt.type == KEYDOWN:
            if evt.key == K_SPACE:
                if won != 0:
                    reset()
            if evt.key == K_v:
                reveal_map = True
        
        if evt.type == KEYUP:
            if evt.key == K_v:
                reveal_map = False

    screen.fill(GREEN)

    for i in range(GRID_DIM[0]):
        for j in range(GRID_DIM[1]):
            if grid[i, j][0] == "r":
                draw.rect(screen, WHITE, (CELL_SIZE*i, CELL_SIZE*j, CELL_SIZE, CELL_SIZE))
                textsurface = myfont.render(str(grid[i, j][1]), False, BLACK)
                screen.blit(textsurface, (CELL_SIZE*i + 0, CELL_SIZE*j))
            elif grid[i, j][0] == "f":
                draw.rect(screen, RED, (CELL_SIZE * i + CELL_SIZE * 0.25, CELL_SIZE*j, CELL_SIZE * 0.5, CELL_SIZE))

    if reveal_map:
        screen.fill(WHITE)
        for i in range(GRID_DIM[0]):
            for j in range(GRID_DIM[1]):
                textsurface = myfont.render(str(grid[i, j][1]), False, BLACK)
                screen.blit(textsurface, (CELL_SIZE*i + 0, CELL_SIZE*j))

    for i in range(GRID_DIM[0]):
        draw.line(screen, BLACK, (CELL_SIZE*i, 0), (CELL_SIZE*i, 15*CELL_SIZE))
    
    for i in range(GRID_DIM[1] + 1):
        draw.line(screen, BLACK, (0, CELL_SIZE*i), (15*CELL_SIZE, i*CELL_SIZE))

    draw.rect(screen, GREY, (0, GRID_DIM[1] * CELL_SIZE, GRID_DIM[0] * CELL_SIZE, 100))
    textsurface = myfont.render(str(flags) + " flags", False, BLACK)
    screen.blit(textsurface, (CELL_SIZE, GRID_DIM[1] * CELL_SIZE + 50))

    if won == -1:
        screen.fill(WHITE)
        for i in range(GRID_DIM[0]):
            for j in range(GRID_DIM[1]):
                textsurface = myfont.render(str(grid[i, j][1]), False, BLACK)
                screen.blit(textsurface, (CELL_SIZE*i + 0, CELL_SIZE*j))
        
        for i in range(GRID_DIM[0]):
            draw.line(screen, BLACK, (CELL_SIZE*i, 0), (CELL_SIZE*i, 15*CELL_SIZE))
    
        for i in range(GRID_DIM[1] + 1):
            draw.line(screen, BLACK, (0, CELL_SIZE*i), (15*CELL_SIZE, i*CELL_SIZE))

        draw.rect(screen, GREY, (0, GRID_DIM[1] * CELL_SIZE, GRID_DIM[0] * CELL_SIZE, 100))
        textsurface = myfont.render("You Lost", False, BLACK)
        screen.blit(textsurface, (width / 2, GRID_DIM[1] * CELL_SIZE))

    if won == 1:
        screen.fill(WHITE)
        textsurface = myfont.render("You Won!", False, BLACK)
        screen.blit(textsurface, (width / 2, GRID_DIM[1] * CELL_SIZE))

    display.flip()

    clock.tick(60)

quit()