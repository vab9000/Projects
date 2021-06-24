"""Gives parameters to draw car"""
import pygame

# COLORS
RED = (255, 0, 0)
BLACK = (0, 0, 0)


class Car:
    def __init__(self):
        self.velocity = 0
        self.x = 20
        self.y = 150

    def render(self, window):
        """Draws the car"""
        pygame.draw.rect(window, RED, (self.x, self.y, 40, 10))
        pygame.draw.circle(window, BLACK, (self.x + 5, self.y + 15), 5)
        pygame.draw.circle(window, BLACK, (self.x + 35, self.y + 15), 5)

    def applyForce(self, velocity, terrain):
        self.x += velocity[0]
        self.y += velocity[1]
        if self.checkCollision(terrain) and velocity[1] > 0:
            self.y -= velocity[1]

    def checkCollision(self, terrain):
        point1 = terrain[int(self.x/5) + 1]
        point2 = terrain[int(self.x/5) + 2]
        point3 = terrain[int(self.x/5) + 3]
        point4 = terrain[int(self.x/5) + 4]
        point5 = terrain[int(self.x/5) + 5]
        point6 = terrain[int(self.x/5) + 6]
        point7 = terrain[int(self.x/5) + 7]
        point8 = terrain[int(self.x/5) + 8]
        highest_point = point1
        if highest_point[1] < point2[1]:
            highest_point = point2
        if highest_point[1] < point3[1]:
            highest_point = point3
        if highest_point[1] < point4[1]:
            highest_point = point4
        if highest_point[1] < point5[1]:
            highest_point = point5
        if highest_point[1] < point6[1]:
            highest_point = point6
        if highest_point[1] < point7[1]:
            highest_point = point7
        if highest_point[1] < point8[1]:
            highest_point = point8
        if self.y + 18 >= highest_point[1]:
            self.y -= 1
            if self.checkCollision(terrain):
                return True
            self.y += 1
            return True
        return False
