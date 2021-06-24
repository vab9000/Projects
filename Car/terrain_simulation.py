"""Compiles all the different generators"""
import pygame
import terrain_generator

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (180, 100, 50)
ORANGE = (255, 200, 70)
YELLOW = (255, 255, 0)

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Terrain Simulation")

# Variables
height = screen.get_height()
width = screen.get_width()
startPoint = [0, height]
endPoint = [width, height]
firstPoint = [0, 300]
velocity = [0, 0]
keys_pressed = list()
terrainPoints = [startPoint, firstPoint, endPoint]


i = 0
while i < 140:
    terrainPoints = terrain_generator.add_point(terrainPoints)
    i += 1
# Program Loop
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    # Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    # Game Logic
    terrain_generator.remove_point(terrainPoints)
    terrain_generator.add_point(terrainPoints)
    # Drawing Logic
    screen.fill(ORANGE)
    pygame.draw.circle(screen, YELLOW, (300, 200), 50)
    pygame.draw.polygon(screen, BROWN, terrainPoints, 0)
    pygame.draw.lines(screen, GREEN, False, terrainPoints[1:-1], 5)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
