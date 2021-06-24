"""Snake Class"""
import random
import pygame

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (177, 177, 177)


class Snake:
    """Snake Class"""
    def __init__(self):
        self.head = [200, 200, 20, 20]
        self.parts = [[200, 220, 20, 20], [200, 240, 20, 20]]
        self.path = list()
        self.dir = 'up'

    def render(self, screen):
        """Draws Snake"""
        i = 0
        while i < len(self.parts):
            pygame.draw.rect(screen, GREEN, self.parts[i])
            if i == 0:
                if (
                    (
                        self.parts[i][0] - self.parts[i + 1][0] == 20 or
                        self.parts[i][0] - self.parts[i + 1][0] == -20
                        ) and
                    (
                        self.parts[i][0] - self.head[0] == 20 or
                        self.parts[i][0] - self.head[0] == -20
                        )
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                elif (
                    (
                        self.parts[i][1] - self.parts[i + 1][1] == 20 or
                        self.parts[i][1] - self.parts[i + 1][1] == -20
                        ) and
                    (
                        self.parts[i][1] - self.head[1] == 20 or
                        self.parts[i][1] - self.head[1] == -20
                        )
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == 20 and
                        self.parts[i][1] - self.head[1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == -20 and
                        self.parts[i][1] - self.head[1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == 20 and
                        self.parts[i][1] - self.head[1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == -20 and
                        self.parts[i][1] - self.head[1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.head[0] == 20 and
                        self.parts[i][1] - self.parts[i + 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.head[0] == -20 and
                        self.parts[i][1] - self.parts[i + 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.head[0] == 20 and
                        self.parts[i][1] - self.parts[i + 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.head[0] == -20 and
                        self.parts[i][1] - self.parts[i + 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
            elif 0 < i < len(self.parts) - 1:
                if (
                    (
                        self.parts[i][0] - self.parts[i + 1][0] == 20 or
                        self.parts[i][0] - self.parts[i + 1][0] == -20
                        ) and
                    (
                        self.parts[i][0] - self.parts[i - 1][0] == 20 or
                        self.parts[i][0] - self.parts[i - 1][0] == -20
                        )
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                elif (
                    (
                        self.parts[i][1] - self.parts[i + 1][1] == 20 or
                        self.parts[i][1] - self.parts[i + 1][1] == -20
                        ) and
                    (
                        self.parts[i][1] - self.parts[i - 1][1] == 20 or
                        self.parts[i][1] - self.parts[i - 1][1] == -20
                        )
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == 20 and
                        self.parts[i][1] - self.parts[i - 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == -20 and
                        self.parts[i][1] - self.parts[i - 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == 20 and
                        self.parts[i][1] - self.parts[i - 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i + 1][0] == -20 and
                        self.parts[i][1] - self.parts[i - 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i - 1][0] == 20 and
                        self.parts[i][1] - self.parts[i + 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i - 1][0] == -20 and
                        self.parts[i][1] - self.parts[i + 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i - 1][0] == 20 and
                        self.parts[i][1] - self.parts[i + 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                elif (
                        self.parts[i][0] - self.parts[i - 1][0] == -20 and
                        self.parts[i][1] - self.parts[i + 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
            elif i == len(self.parts) - 1:
                if (
                    self.parts[i][0] - self.parts[i - 1][0] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                        )
                    )
                elif (
                    self.parts[i][0] - self.parts[i - 1][0] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                        )
                    )
                elif (
                    self.parts[i][1] - self.parts[i - 1][1] == 20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1] + 18, 20, 2
                        )
                    )
                elif (
                    self.parts[i][1] - self.parts[i - 1][1] == -20
                ):
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0] + 18, self.parts[i][1], 2, 20
                            )
                        )
                    pygame.draw.rect(
                        screen, WHITE, (
                            self.parts[i][0], self.parts[i][1], 20, 2
                        )
                    )
            pygame.draw.rect(
                screen, WHITE, (
                    self.parts[i][0], self.parts[i][1], 2, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.parts[i][0] + 18, self.parts[i][1], 2, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.parts[i][0], self.parts[i][1] + 18, 2, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.parts[i][0] + 18, self.parts[i][1] + 18, 2, 2
                    )
                )
            i += 1
        pygame.draw.rect(screen, GRAY, self.head)
        if (
            self.parts[0][0] - self.head[0] == -20
        ):
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1], 20, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1] + 18, 20, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0] + 18, self.head[1], 2, 20
                )
            )
        elif (
            self.parts[0][0] - self.head[0] == 20
        ):
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1], 20, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1] + 18, 20, 2
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1], 2, 20
                )
            )
        elif (
            self.parts[0][1] - self.head[1] == -20
        ):
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1], 2, 20
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0] + 18, self.head[1], 2, 20
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1] + 18, 20, 2
                )
            )
        elif (
            self.parts[0][1] - self.head[1] == 20
        ):
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1], 2, 20
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0] + 18, self.head[1], 2, 20
                    )
                )
            pygame.draw.rect(
                screen, WHITE, (
                    self.head[0], self.head[1], 20, 2
                )
            )

    def move(self):
        """Moves Snake"""
        self.path = self.parts.copy()
        self.parts[0] = self.head.copy()
        i = 1
        while i < len(self.parts):
            self.parts[i] = self.path[i - 1]
            i += 1
        if self.dir == 'up':
            self.head[1] -= 20
        elif self.dir == 'left':
            self.head[0] -= 20
        elif self.dir == 'right':
            self.head[0] += 20
        elif self.dir == 'down':
            self.head[1] += 20

    def check_collision(self):
        """Checks for collision"""
        for part in self.parts:
            if part == self.head:
                return True
        if not 0 <= self.head[0] < 520:
            return True
        if not 0 <= self.head[1] < 520:
            return True
        return False

    def eating_berry(self, berry):
        """Checks for eating berry"""
        if self.head[0] == berry.x_pos and self.head[1] == berry.y_pos:
            return True
        return False

    def add_part(self):
        """Adds a part to the snake"""
        self.parts.append(self.path[-1].copy())


class Berry:
    """Berry Class"""
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.eaten = False

    def render(self, screen):
        """Draws Berry"""
        if not self.eaten:
            pygame.draw.rect(screen, RED, (self.x_pos, self.y_pos, 20, 20))

    def randomize(self, snake):
        """Puts berry in a random spot"""
        empty_spots = list()
        i = 0
        while i < 520:
            j = 0
            while j < 520:
                if [i, j, 20, 20] not in snake.parts:
                    if not [i, j, 20, 20] == snake.head:
                        empty_spots.append([i, j])
                j += 20
            i += 20
        if len(empty_spots) != 0:
            rand_move = random.randrange(0, len(empty_spots))
            self.x_pos = empty_spots[rand_move][0]
            self.y_pos = empty_spots[rand_move][1]
        else:
            self.eaten = True
