"""Snake AI 2"""


def ai_move():
    move_queue = list()
    i = 0
    while i < 13:
        moves = move_column()
        for move in moves:
            move_queue.append(move)
        i += 1
    move_queue.pop(0)
    move_queue.pop(-1)
    move_queue.append('down')
    i = 0
    while i < 25:
        move_queue.append('right')
        i += 1
    move_queue.append('up')
    move_queue.append('up')
    return move_queue


def move_column():
    return_moves = list()
    i = 0
    while i < 24:
        return_moves.append('up')
        i += 1
    return_moves.append('left')
    i = 0
    while i < 24:
        return_moves.append('down')
        i += 1
    return_moves.append('left')
    return return_moves
