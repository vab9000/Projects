"""Memory game"""
import random
import pygame

pygame.init()
pygame.font.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a window
size = (1600, 100)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Memory Game")
myfont = pygame.font.SysFont('Arial', 30)

# Variables
height = screen.get_height()
width = screen.get_width()
cards = list()
i = 0
while i < 8:
    cards.append(i)
    cards.append(i)
    i += 1
revealed_cards = list()
revealed_numbers = list()
revealed = list()
i = 0
while i < 8:
    revealed_cards.append(False)
    revealed_cards.append(False)
    revealed.append(False)
    revealed.append(False)
    i += 1
full_true = list()
i = 0
while i < 8:
    full_true.append(True)
    full_true.append(True)
    i += 1
random.shuffle(cards)
mouse = pygame.mouse.get_pos()

# Program Loop
CARRY_ON = True
clock = pygame.time.Clock()

while CARRY_ON:
    # Main Event Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CARRY_ON = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            card_num = int(mouse[0]/100)
            if not revealed[card_num]:
                revealed_cards[card_num] = True
                revealed[card_num] = True
                if len(revealed_numbers) == 2:
                    if revealed_numbers[0][0] == revealed_numbers[1][0]:
                        revealed_cards[revealed_numbers[0][1]] = False
                        revealed_cards[revealed_numbers[1][1]] = False
                        revealed_numbers = list()
                    else:
                        revealed[revealed_numbers[0][1]] = False
                        revealed[revealed_numbers[1][1]] = False
                        revealed_cards[revealed_numbers[0][1]] = False
                        revealed_cards[revealed_numbers[1][1]] = False
                        revealed_numbers = list()
    # Game Logic
    mouse = pygame.mouse.get_pos()

    # Drawing Logic
    screen.fill(WHITE)
    LENGTH = 0
    i = 0
    revealed_numbers = list()
    for card in cards:
        if not revealed[i]:
            pygame.draw.rect(screen, BLACK, [LENGTH + 5, 5, 90, 90], 0)
        else:
            if revealed_cards[i]:
                revealed_numbers.append([cards[i], i])
            textsurface = myfont.render(str(card), False, (0, 0, 0))
            screen.blit(textsurface, (LENGTH + 35, 35))
        LENGTH += 100
        i += 1

    if revealed == full_true:
        screen.fill(WHITE)
        textsurface = myfont.render('You Win', False, (0, 0, 0))
        screen.blit(textsurface, (750, 35))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
