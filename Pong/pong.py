'''The game pong'''
import pygame
import pong_ai

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

# Open a window
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')
myfont = pygame.font.SysFont('Arial', 30)

# Variables
height = screen.get_height()
width = screen.get_width()
score = [0, 0]
paddle1 = [25, 150, 10, 100]
PADDLE_VEL1 = 0
paddle2 = [465, 150, 10, 100]
PADDLE_VEL2 = 0
pong = [240, 190, 20, 20]
velocity = [1, 0]
keys_pressed = list()

# Program Loop
CARRY_ON = True
clock = pygame.time.Clock()

while CARRY_ON:
    # Main Event Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CARRY_ON = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                keys_pressed.append(pygame.K_DOWN)
            elif event.key == pygame.K_UP:
                keys_pressed.append(pygame.K_UP)
            elif event.key == pygame.K_s:
                keys_pressed.append(pygame.K_s)
            elif event.key == pygame.K_w:
                keys_pressed.append(pygame.K_w)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                keys_pressed.remove(pygame.K_DOWN)
            elif event.key == pygame.K_UP:
                keys_pressed.remove(pygame.K_UP)
            elif event.key == pygame.K_s:
                keys_pressed.remove(pygame.K_s)
            elif event.key == pygame.K_w:
                keys_pressed.remove(pygame.K_w)

    # Game Logic
    if pygame.K_DOWN in keys_pressed:
        PADDLE_VEL2 = 1
    if pygame.K_UP in keys_pressed:
        PADDLE_VEL2 = -1
    if pygame.K_s in keys_pressed:
        PADDLE_VEL1 = 1
    if pygame.K_w in keys_pressed:
        PADDLE_VEL1 = -1
    if velocity[0] > 0:
        PADDLE_VEL2 = pong_ai.pong_ai(paddle2, pong, velocity)
    else:
        PADDLE_VEL2 = 0
    if velocity[0] < 0:
        PADDLE_VEL1 = pong_ai.pong_ai(paddle1, pong, velocity)
    else:
        PADDLE_VEL1 = 0
    if pong[0] > 480:
        score[0] += 1
        pong = [240, 190, 20, 20]
        velocity = [1, 0]
    if pong[0] < 0:
        score[1] += 1
        pong = [240, 190, 20, 20]
        velocity = [-1, 0]
    if (paddle2[1] < pong[1] < paddle2[1] + 100) and 445 < pong[0] < 465:
        velocity[0] += 0.1
        velocity[0] = -velocity[0]
        if PADDLE_VEL2 == 1:
            velocity[1] += 1
        elif PADDLE_VEL2 == -1:
            velocity[1] -= 1
    elif (
        paddle2[1] < pong[1] + 20 < paddle2[1] + 100
    ) and 445 < pong[0] < 465:
        velocity[0] += 0.1
        velocity[0] = -velocity[0]
        if PADDLE_VEL2 == 1:
            velocity[1] += 1
        elif PADDLE_VEL2 == -1:
            velocity[1] -= 1
    if (paddle1[1] < pong[1] < paddle1[1] + 100) and 15 < pong[0] < 35:
        velocity[0] -= 0.1
        velocity[0] = -velocity[0]
        if PADDLE_VEL1 == 1:
            velocity[1] += 1
        elif PADDLE_VEL1 == -1:
            velocity[1] -= 1
    elif (paddle1[1] < pong[1] + 20 < paddle1[1] + 100) and 15 < pong[0] < 35:
        velocity[0] -= 0.1
        velocity[0] = -velocity[0]
        if PADDLE_VEL1 == 1:
            velocity[1] += 1
        elif PADDLE_VEL1 == -1:
            velocity[1] -= 1
    if pong[1] < 0 or pong[1] > 380:
        velocity[1] = -velocity[1]
    pong[0] += velocity[0]
    pong[1] += velocity[1]
    paddle1[1] += PADDLE_VEL1
    paddle2[1] += PADDLE_VEL2
    if paddle1[1] < 0:
        paddle1[1] = 0
    elif paddle1[1] > 300:
        paddle1[1] = 300
    if paddle2[1] < 0:
        paddle2[1] = 0
    elif paddle2[1] > 300:
        paddle2[1] = 300
    PADDLE_VEL1 = 0
    PADDLE_VEL2 = 0

    # Drawing Logic
    screen.fill(BLACK)
    textsurface = myfont.render(
        str(score[0]) + ' – ' + str(score[1]), False, WHITE
        )
    screen.blit(textsurface, (225, 450))
    pygame.draw.rect(screen, WHITE, paddle1, 0)
    pygame.draw.rect(screen, WHITE, paddle2, 0)
    pygame.draw.rect(screen, WHITE, pong, 0)
    pygame.draw.rect(screen, GRAY, (0, 400, 500, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
