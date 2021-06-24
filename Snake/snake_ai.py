"""Ai for snake"""
import random
import snake_classes


def ai_move(snake, berry, random_moves=0, first_try=True):
    """Snake ai function"""
    new_snake = snake_copy(snake)
    berry_copy = snake_classes.Berry(berry.x_pos, berry.y_pos)
    i = 0
    move_queue = list()
    while True:
        if i < random_moves:
            move_queue.append(move_in_berry_direction(new_snake, berry_copy))
            if not move_queue[-1]:
                return ai_move(snake, berry_copy, 0)
            new_snake.dir = move_queue[-1]
            new_snake.move()
            if new_snake.eating_berry(berry_copy):
                break
            if new_snake.check_collision():
                return ai_move(snake, berry_copy, random_moves + 1, False)
        else:
            possible_move_list = possible_moves(snake)
            try:
                rand_move = random.randrange(0, len(possible_move_list))
            except ValueError:
                return ai_move(snake, berry_copy, random_moves + 1, False)
            move_queue.append(possible_move_list[rand_move])
            if not move_queue[-1]:
                return ai_move(snake, berry_copy, 0)
            new_snake.dir = move_queue[-1]
            new_snake.move()
            if new_snake.eating_berry(berry_copy):
                break
            if new_snake.check_collision():
                return ai_move(snake, berry_copy, random_moves + 1, False)
        i += 1
    if first_try:
        try:
            new_snake.add_part()
            berry_copy.randomize(new_snake)
            ai_move(new_snake, berry_copy, 0, False)
        except RecursionError:
            return ai_move(snake, berry, random_moves + 1, False)
    return move_queue


def ai_random_move(snake, berry):
    new_snake = snake_copy(snake)
    move_queue = list()
    while True:
        possible_move_list = possible_moves(snake)
        try:
            rand_move = random.randrange(0, len(possible_move_list))
        except ValueError:
            return ai_random_move(snake, berry)
        move_queue.append(possible_move_list[rand_move])
        new_snake.dir = move_queue[-1]
        new_snake.move()
        if new_snake.eating_berry(berry):
            break
        if new_snake.check_collision():
            return ai_random_move(snake, berry)
    return move_queue


def move_in_berry_direction(snake, berry):
    possible_move_list = possible_moves(snake)
    bad_moves = list()
    if snake.head[0] - berry.x_pos >= 20:
        if 'left' in possible_move_list:
            return 'left'
        bad_moves.append('left')
    if snake.head[0] - berry.x_pos <= -20:
        if 'right' in possible_move_list:
            return 'right'
        bad_moves.append('right')
    if snake.head[1] - berry.y_pos >= 20:
        if 'up' in possible_move_list:
            return 'up'
        bad_moves.append('up')
    if snake.head[1] - berry.y_pos <= -20:
        if 'down' in possible_move_list:
            return 'down'
        bad_moves.append('down')
    for move in bad_moves:
        if move in possible_move_list:
            possible_move_list.remove(move)
    try:
        rand_move = random.randrange(0, len(possible_move_list))
    except ValueError:
        return False
    return possible_move_list[rand_move]


def possible_moves(snake):
    possible_move_list = list()
    left_snake = snake_copy(snake, 'left')
    left_snake.move()
    if not left_snake.check_collision():
        possible_move_list.append('left')
    right_snake = snake_copy(snake, 'right')
    right_snake.move()
    if not right_snake.check_collision():
        possible_move_list.append('right')
    up_snake = snake_copy(snake, 'up')
    up_snake.move()
    if not up_snake.check_collision():
        possible_move_list.append('up')
    down_snake = snake_copy(snake, 'down')
    down_snake.move()
    if not down_snake.check_collision():
        possible_move_list.append('down')
    return possible_move_list


def snake_copy(snake, direct='up'):
    new_snake = snake_classes.Snake()
    new_snake.parts = snake.parts.copy()
    new_snake.head = snake.head.copy()
    new_snake.dir = direct
    return new_snake
