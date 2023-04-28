"""Alien class"""
import pygame

RED = (255, 0, 0)


class Alien:
    """Alien Class"""
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.img = pygame.image.load('AlienInvaders/alien.jpeg')
        self.img = pygame.transform.scale(self.img, (71, 51))

    def render(self, screen):
        """Renders image"""
        screen.blit(self.img, (self.x_pos, self.y_pos))


class Bullet:
    """Bullet shot by alien class"""
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def render(self, screen):
        """Renders bullet"""
        pygame.draw.rect(screen, RED, (self.x_pos, self.y_pos, 10, 50), 0)
