import pygame
import random
import time

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DULL_GREEN = (0, 127, 0)
DULL_RED = (127, 0, 0)
DULL_BLUE = (0, 0, 127)
DULL_YELLOW = (127, 127, 0)

# Open a window
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simon")
myfont = pygame.font.SysFont('Arial', 30)

# Variables
height = screen.get_height()
width = screen.get_width()
pattern = list()
pattern_len = 0
player_pattern = list()
pattern_finished = True
new_time = time.time()
score = 0
mouse = pygame.mouse.get_pos()
pattern.append(random.randint(1, 4))
pattern_len += 1

# Program Loop
carryOn = True
clock = pygame.time.Clock()


def same_ending_pattern():
    if pattern[-1] == pattern[-2]:
        pattern.pop(-1)
        pattern.append(random.randint(1, 4))
        same_ending_pattern()


while carryOn:
    # Main Event Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 < mouse[0] < 400 and 0 < mouse[1] < 400:
                player_pattern.append(1)
            elif 400 < mouse[0] < 800 and 0 < mouse[1] < 400:
                player_pattern.append(2)
            elif 0 < mouse[0] < 400 and 400 < mouse[1] < 800:
                player_pattern.append(3)
            elif 400 < mouse[0] < 800 and 400 < mouse[1] < 800:
                player_pattern.append(4)
    # Game Logic
    mouse = pygame.mouse.get_pos()
    # Drawing Logic
    screen.fill(BLACK)
    pygame.draw.rect(screen, DULL_YELLOW, (5, 5, 390, 390), 0)
    pygame.draw.rect(screen, DULL_BLUE, (405, 5, 390, 390), 0)
    pygame.draw.rect(screen, DULL_RED, (5, 405, 390, 390), 0)
    pygame.draw.rect(screen, DULL_GREEN, (405, 405, 390, 390), 0)
    if len(player_pattern) == pattern_len:
        if player_pattern == pattern:
            player_pattern = list()
            pattern_finished = True
            pattern.append(random.randint(1, 4))
            same_ending_pattern()
            pattern_len += 1
            score += 1
            time.sleep(0.3)
            new_time = time.time()
        else:
            screen.fill(BLACK)
            textsurface = myfont.render('You Failed!', False, WHITE)
            screen.blit(textsurface, (350, 385))
            textsurface = myfont.render('Score: ' + str(score), False, WHITE)
            screen.blit(textsurface, (350, 425))
    if len(player_pattern) > pattern_len:
        screen.fill(BLACK)
        textsurface = myfont.render('You Failed!', False, WHITE)
        screen.blit(textsurface, (350, 385))
        textsurface = myfont.render('Score: ' + str(score), False, WHITE)
        screen.blit(textsurface, (350, 425))

    if pattern_finished:
        if pattern_len - 1 < int(time.time() - new_time):
            pattern_finished = False
        elif pattern[int(time.time() - new_time)] == 1:
            pygame.draw.rect(screen, YELLOW, (5, 5, 390, 390), 0)
        elif pattern[int(time.time() - new_time)] == 2:
            pygame.draw.rect(screen, BLUE, (405, 5, 390, 390), 0)
        elif pattern[int(time.time() - new_time)] == 3:
            pygame.draw.rect(screen, RED, (5, 405, 390, 390), 0)
        elif pattern[int(time.time() - new_time)] == 4:
            pygame.draw.rect(screen, GREEN, (405, 405, 390, 390), 0)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
