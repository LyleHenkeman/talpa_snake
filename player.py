import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


class Player:
    def __init__(self):
        self.col = 0
        self.row = 0

    def is_move_possible(idx, move):
    flag = False
    if move == LEFT:
        flag = True if idx%WIDTH > 1 else False
    elif move == RIGHT:
        flag = True if idx%WIDTH < (WIDTH-2) else False
    elif move == UP:
        flag = True if idx > (2*WIDTH-1) else False
    elif move == DOWN:
        flag = True if idx < (FIELD_SIZE-2*WIDTH) else False
    return flag

    def choose_shortest_safe_move(psnake, pboard):
    best_move = ERR
    min = SNAKE
    for i in xrange(4):
        if is_move_possible(psnake[HEAD], mov[i]) and pboard[psnake[HEAD]+mov[i]]<min:
            min = pboard[psnake[HEAD]+mov[i]]
            best_move = mov[i]
    return best_move

    def choose_longest_safe_move(psnake, pboard):
    best_move = ERR
    max = -1
    for i in xrange(4):
        if is_move_possible(psnake[HEAD], mov[i]) and pboard[psnake[HEAD]+mov[i]]<UNDEFINED and pboard[psnake[HEAD]+mov[i]]>max:
            max = pboard[psnake[HEAD]+mov[i]]
            best_move = mov[i]
    return best_move

    def follow_tail():
    global tmpboard, tmpsnake, tmpsnake_size
    tmpsnake_size = snake_size
    tmpsnake = snake[:]
    board_reset(tmpsnake, tmpsnake_size, tmpboard)
    board_refresh(tmpsnake[tmpsnake_size-1], tmpsnake, tmpboard) 
    tmpboard[tmpsnake[tmpsnake_size-1]] = SNAKE

    def any_possible_move();
