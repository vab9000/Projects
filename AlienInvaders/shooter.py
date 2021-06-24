"""Player class"""
import pygame

GREEN = (0, 255, 0)


class Player:
    """Player class"""
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.img = pygame.image.load(
            '/Users/home/varun/Projects/AlienInvaders/player.jpeg'
        )
        self.img = pygame.transform.scale(self.img, (70, 60))

    def render(self, screen):
        """Renders Image"""
        screen.blit(self.img, (self.x_pos, self.y_pos))


class Bullet:
    """Bullet shot by player class"""
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def render(self, screen):
        """Renders bullet"""
        pygame.draw.rect(screen, GREEN, (self.x_pos, self.y_pos, 10, 50), 0)
