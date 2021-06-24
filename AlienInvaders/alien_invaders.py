"""Alien Invaders"""
import time
import random
import pygame
import alien
import shooter

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Open a window
size = (1200, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Alien Invaders")
arial200 = pygame.font.SysFont('Arial', 200)
arial30 = pygame.font.SysFont('Arial', 30)

# Variables
keys_pressed = list()
height = screen.get_height()
width = screen.get_width()
alien1 = alien.Alien(20, 20)
alien2 = alien.Alien(100, 20)
alien3 = alien.Alien(20, 200)
alien4 = alien.Alien(100, 200)
aliens = [alien1, alien2, alien3, alien4]
ALIEN_DIR = 1
player = shooter.Player(20, height - 60)
bullets = list()
alien_bullets = list()
ALIVE = True
AMMO = 5
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
            if event.key == pygame.K_RIGHT:
                keys_pressed.append(pygame.K_RIGHT)
            if event.key == pygame.K_LEFT:
                keys_pressed.append(pygame.K_LEFT)
            if event.key == pygame.K_SPACE:
                if AMMO > 0:
                    bullets.append(
                        shooter.Bullet(
                            player.x_pos + 30, height - 110
                            )
                        )
                    AMMO -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                keys_pressed.remove(pygame.K_RIGHT)
            if event.key == pygame.K_LEFT:
                keys_pressed.remove(pygame.K_LEFT)
    # Drawing Logic
    screen.fill(BLACK)
    if len(aliens) == 0:
        screen.fill(BLACK)
        textsurface = arial200.render('You win', False, WHITE)
        screen.blit(textsurface, (200, 400))
    elif not ALIVE:
        screen.fill(BLACK)
        textsurface = arial200.render('You lose', False, WHITE)
        screen.blit(textsurface, (200, 400))
    else:
        textsurface = arial30.render('Ammo: ' + str(AMMO), False, WHITE)
        screen.blit(textsurface, (20, 400))
        if len(aliens) > 0:
            alien_to_shoot = random.randint(0, len(aliens) - 1)
        else:
            alien_to_shoot = random.randint(-1, -1)
        i = 0
        for alien_character in aliens:
            alien_character.render(screen)
            if alien_to_shoot == i:
                if time.time() - new_time >= 1:
                    alien_bullets.append(
                        alien.Bullet(
                            alien_character.x_pos + 30,
                            alien_character.y_pos + 50
                            )
                        )
                    new_time = time.time()
            alien_character.x_pos += ALIEN_DIR
            if alien_character.x_pos >= width - 71:
                ALIEN_DIR = -1
            elif alien_character.x_pos <= 0:
                ALIEN_DIR = 1
            i += 1
        if ALIVE:
            player.render(screen)
            if pygame.K_RIGHT in keys_pressed:
                player.x_pos += 2
            if pygame.K_LEFT in keys_pressed:
                player.x_pos -= 2
        for bullet in bullets:
            bullet.y_pos -= 3
            if bullet.y_pos <= 0:
                bullets.remove(bullet)
                AMMO += 1
            else:
                for alien_character in aliens:
                    if (
                        (
                            alien_character.x_pos
                            < bullet.x_pos <
                            alien_character.x_pos + 70
                            ) or (
                                alien_character.x_pos
                                < bullet.x_pos + 10 <
                                alien_character.x_pos + 70
                                )
                        ) and (
                            (
                                alien_character.y_pos
                                < bullet.y_pos <
                                alien_character.y_pos + 50
                                ) or (
                                    alien_character.y_pos
                                    < bullet.y_pos + 50 <
                                    alien_character.y_pos + 50
                                    )
                            ):
                        bullets.remove(bullet)
                        aliens.remove(alien_character)
                        AMMO += 1
                        break
            bullet.render(screen)
        for bullet in alien_bullets:
            bullet.y_pos += 3
            if (
                (
                    player.x_pos
                    < bullet.x_pos <
                    player.x_pos + 70
                    ) or (
                        player.x_pos
                        < bullet.x_pos + 10 <
                        player.x_pos + 70
                        )
                ) and (
                    (
                        player.y_pos
                        < bullet.y_pos <
                        player.y_pos + 60
                        ) or (
                            player.y_pos
                            < bullet.y_pos + 50 <
                            player.y_pos + 60
                            )
                    ):
                alien_bullets.remove(bullet)
                ALIVE = False
            elif bullet.y_pos >= height - 50:
                alien_bullets.remove(bullet)
            bullet.render(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
