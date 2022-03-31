from typing import Sequence
import classes
import time
import random
import pygame

pygame.init()

size = (500, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")

height = screen.get_height()
width = screen.get_width()
blocks = []
new_time = time.time()
block_types = [classes.O, classes.I, classes.S, classes.Z, classes.T, classes.L, classes.J]

carryOn = True
clock = pygame.time.Clock()

def print2D(array: Sequence[Sequence]) -> None:
    i = 0
    while i < height/50:
        j = 0
        while j < width/50:
            print(str(array[i][j]), end=', ')
            j += 1
        i += 1
        print()

def row_made() -> None:
    array = list()
    i = 0
    while i < height/50:
        row = list()
        j = 0
        while j < width/50:
            row.append(False)
            j += 1
        array.append(row)
        i += 1
    for block in blocks:
        array[block.y][block.x] = True
    k = 0
    for row in array:
        false_encountered = False
        for block in row:
            if not block:
                false_encountered = True
                break
        if not false_encountered:
            remove_row(k)
            row_made()
            break
        k += 1

def remove_row(num: int) -> None:
    i = 0
    while i < len(blocks):
        if blocks[i].y == num:
            blocks.remove(blocks[i])
            i -= 1
        i += 1
    for block in blocks:
        if block.y < num:
            block.y += 1

def random_block() -> classes.MultiBlock:
    rand = random.randrange(0, len(block_types))
    return block_types[rand](4, 0)

def intersecting(dir: str) -> bool:
    if dir == 'down':
        new_block = current_block.copy()
        for block in new_block.blocks:
            block.y += 1
    elif dir == 'left':
        new_block = current_block.copy()
        for block in new_block.blocks:
            block.x -= 1
    elif dir == 'right':
        new_block = current_block.copy()
        for block in new_block.blocks:
            block.x += 1
    for block in new_block.blocks:
        if block.y > height/50 - 1:
            return True
        elif block.x < 0 or block.x > width/50 - 1:
            return True
        else:
            for placed_block in blocks:
                if block.x == placed_block.x and block.y == placed_block.y:
                    return True
    return False

current_block = classes.J(4, 0)

while carryOn:
    # Main Event Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not intersecting('left'):
                    for block in current_block.blocks:
                        block.x -= 1
            elif event.key == pygame.K_RIGHT:
                if not intersecting('right'):
                    for block in current_block.blocks:
                        block.x += 1
            elif event.key == pygame.K_UP:
                current_block.rotate(blocks, width, height)
            elif event.key == pygame.K_DOWN:
                if not intersecting('down'):
                    for block in current_block.blocks:
                        block.y += 1

    if time.time() - 0.5 > new_time:
        new_time = time.time()
        if not intersecting('down'):
            for block in current_block.blocks:
                block.y += 1
        else:
            for block in current_block.blocks:
                blocks.append(block)
            current_block = random_block()
            row_made()

    screen.fill((0,0,0))

    for block in blocks:
        pygame.draw.rect(screen, block.color, (block.x * 50, block.y * 50, 50, 50))

    for block in current_block.blocks:
        pygame.draw.rect(screen, block.color, (block.x * 50, block.y * 50, 50, 50))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
