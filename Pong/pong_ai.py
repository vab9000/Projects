'''Pong AI'''
import random


def pong_ai(paddle, pong, velocity):
    '''Returns AI moves'''
    pong_copy = pong.copy()
    velocity_copy = velocity.copy()
    random_loop = random.randint(0, 1) * random.randint(0, 1)
    while True:
        if random_loop == 1:
            if pong_copy[1] < 0 or pong_copy[1] > 380:
                velocity_copy[1] = -velocity_copy[1]
            pong_copy[0] += velocity_copy[0]
            pong_copy[1] += velocity_copy[1]
            if pong_copy[0] >= 445 or pong_copy[0] <= 35:
                if pong_copy[1] - paddle[1] > 40:
                    move_dir = 1
                else:
                    move_dir = -1
                return move_dir
        else:
            if pong_copy[1] < 0 or pong_copy[1] > 380:
                velocity_copy[1] = -velocity_copy[1]
            pong_copy[0] += velocity_copy[0]
            pong_copy[1] += velocity_copy[1]
            if pong_copy[0] >= 445 or pong_copy[0] <= 35:
                if pong_copy[1] - paddle[1] == 40:
                    move_dir = 0
                elif pong_copy[1] - paddle[1] > 40:
                    move_dir = 1
                else:
                    move_dir = -1
                return move_dir
