"""Snake AI test"""
import time
import pygame
import snake_classes
import new_snake_ai


pygame.init()

WHITE = (255, 255, 255)

# Open a window
size = (520, 520)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

# Variables
player = snake_classes.Snake()
berry = snake_classes.Berry(20, 20)
ALIVE = True
WON = False
berry.randomize(player)
move_queue = list()
new_time = time.time()
i = 0
while i < 14:
    move_queue.append('right')
    i += 1
i = 0
while i < 13:
    move_queue.append('down')
    i += 1
move_queue.append('right')
CARRY_ON = True

# Main Event Loop
while CARRY_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CARRY_ON = False
    # Drawing Logic
    screen.fill(WHITE)
    if WON:
        berry.render(screen)
        player.render(screen)
        if len(move_queue) == 0:
            move_queue = new_snake_ai.ai_move()
        player.dir = move_queue[0]
        move_queue.pop(0)
        player.move()
    elif ALIVE:
        berry.render(screen)
        player.render(screen)
        if time.time() - new_time >= 0.01:
            if len(move_queue) == 0:
                move_queue = new_snake_ai.ai_move()
            if player.check_collision():
                ALIVE = False
            player.dir = move_queue[0]
            move_queue.pop(0)
            player.move()
            if player.eating_berry(berry):
                player.add_part()
                berry.randomize(player)
                if len(player.parts) >= (26*26)-1:
                    WON = True
            new_time = time.time()
    else:
        berry.render(screen)
        player.render(screen)
    pygame.display.flip()
pygame.quit()
