"""
Snake AI test
Caution: Will crash a lot
"""
import pygame
import snake_classes
import snake_ai


def game_run():
    """Function that can be recursed"""
    pygame.init()

    white = (255, 255, 255)

    # Open a window
    size = (520, 520)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake")

    # Variables
    player = snake_classes.Snake()
    berry = snake_classes.Berry(20, 20)
    alive = True
    won = False
    berry.randomize(player)
    move_queue = list()
    carry_on = True

    # Main Event Loop
    while carry_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry_on = False
        # Drawing Logic
        screen.fill(white)
        if won:
            player.render(screen)
        elif alive:
            berry.render(screen)
            player.render(screen)
            if len(move_queue) == 0:
                try:
                    move_queue = snake_ai.ai_move(player, berry)
                except RecursionError:
                    try:
                        move_queue = snake_ai.ai_random_move(player, berry)
                    except RecursionError:
                        game_run()
                        break
            if player.check_collision():
                alive = False
            player.dir = move_queue[0]
            move_queue.pop(0)
            player.move()
            if player.eating_berry(berry):
                player.add_part()
                berry.randomize(player)
                if len(player.parts) >= (26*26)-1:
                    won = True
        else:
            berry.render(screen)
            player.render(screen)
        pygame.display.flip()
    pygame.quit()


game_run()
