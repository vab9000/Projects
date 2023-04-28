# Pygame test
from numpy import zeros
from pygame import MOUSEBUTTONDOWN, init, quit, time, display, event, QUIT, draw, mouse, font

init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (122, 122, 122)

CELL_SIZE = 50
GRID_DIM = (5, 5)

size = (GRID_DIM[0]*CELL_SIZE, GRID_DIM[1]*CELL_SIZE)
screen = display.set_mode(size)
display.set_caption("Grid")
height = screen.get_height()
width = screen.get_width()
carry_on = True
clock = time.Clock()
color = GREY
mouse_pos = mouse.get_pos()
myfont = font.SysFont('Courier New', 30)

grid = zeros((GRID_DIM[0], GRID_DIM[1]), dtype=int)
number = 1

while carry_on:
    # Main Event Loop

    for evt in event.get():
        if evt.type == QUIT:
            carry_on = False
        
        if evt.type == MOUSEBUTTONDOWN:
            mouse_pos = mouse.get_pos()
            if grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE] == 0:
                grid[mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE] = number
                number += 1 

    screen.fill(WHITE)

    for i in range(GRID_DIM[0]):
        draw.line(screen, BLACK, (CELL_SIZE*i, 0), (CELL_SIZE*i, 15*CELL_SIZE))
    
    for i in range(GRID_DIM[1]):
        draw.line(screen, BLACK, (0, CELL_SIZE*i), (15*CELL_SIZE, i*CELL_SIZE))

    for i in range(GRID_DIM[0]):
        for j in range(GRID_DIM[1]):
            textsurface = myfont.render(str(grid[i, j]), False, BLACK)
            screen.blit(textsurface, (CELL_SIZE*i + 0, CELL_SIZE*j))

    display.flip()

    clock.tick(60)

quit()