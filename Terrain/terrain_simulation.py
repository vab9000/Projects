"""Compiles all the different generators"""
import time
import random
import pygame
import terrain_generator

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 125, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (180, 100, 50)
DARKEST_GREEN = (0, 100, 0)
DARK_GREEN = (0, 150, 0)
ORANGE = (255, 200, 70)
YELLOW = (255, 255, 0)
GRAY = (125, 125, 125)

# Open a window
width = 1920
length = 1200
size = (width, length)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Terrain Simulation")

# Variables
height = screen.get_height()
width = screen.get_width()
startPoint = [0, height]
endPoint = [width, height]
firstPoint = [0, length/2]
terrainPoints = [startPoint, firstPoint, endPoint]
startPoint = [0, height]
endPoint = [width, height]
firstPoint = [0, length/2]
midgroundPoints = [startPoint, firstPoint, endPoint]
startPoint = [0, height]
endPoint = [width, height]
firstPoint = [0, length - 240]
rockPoints = [startPoint, firstPoint, endPoint]
startPoint = [0, height]
endPoint = [width, height]
firstPoint = [0, length/2]
backgroundPoints = [startPoint, firstPoint, endPoint]
current_time = time.time()
distance = 6
backgroundDistance = 4
midgroundDistance = 3

i = 0
while i < width/distance:
    terrainPoints = terrain_generator.add_point(terrainPoints, distance, length, length/2-60, length-120)
    i += 1

i = 0
while i < width/distance:
    rockPoints = terrain_generator.add_point(rockPoints, distance, length, length-240, length-120)
    i += 1

i = 0
while i < width/backgroundDistance:
    backgroundPoints = terrain_generator.add_point(backgroundPoints, backgroundDistance, length, length/2-240, length/2-120)
    i += 1

i = 0
while i < width/midgroundDistance:
    midgroundPoints = terrain_generator.add_point(midgroundPoints, midgroundDistance, length, length/2-360, length/2-240)
    i += 1
# Program Loop
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                carryOn = False
    # Game Logic
    if time.time() - current_time > -1:
        terrain_generator.remove_point(terrainPoints, distance)
        terrain_generator.add_point(terrainPoints, distance, length, length/2, length-120)
        terrain_generator.remove_point(rockPoints, distance)
        terrain_generator.add_point(rockPoints, distance, length, length-240, length-120)
        terrain_generator.remove_point(backgroundPoints, backgroundDistance)
        terrain_generator.add_point(backgroundPoints, backgroundDistance, length, length/2 - 240, length/2 - 120)
        terrain_generator.remove_point(midgroundPoints, midgroundDistance)
        terrain_generator.add_point(midgroundPoints, midgroundDistance, length, length/2-360, length/2-240)
        current_time = time.time()
    # Drawing Logic
    screen.fill(ORANGE)
    pygame.draw.circle(screen, YELLOW, (300, 200), 50)
    pygame.draw.polygon(screen, DARKEST_GREEN, midgroundPoints, 0)
    pygame.draw.polygon(screen, DARK_GREEN, backgroundPoints, 0)
    pygame.draw.lines(screen, GREEN, False, terrainPoints[1:-1], 5)
    pygame.draw.rect(screen, BLUE, (0, length/2, width, length))
    BLUE = (100, 100, ((abs((current_time%10)-5))+5)*15+100)
    pygame.draw.polygon(screen, BROWN, terrainPoints, 0)
    pygame.draw.polygon(screen, GRAY, rockPoints, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
