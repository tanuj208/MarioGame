import sys, termios, tty, os, time, datetime, random, colorama as cl, numpy as np
from characters import *
from ascii import *
import math


f = open("background.txt",'r')

def printBoard(mario_x,mario_y):
	for i in range(HEIGHT-1):
		final_board.append('')
		if i < mario_x or i > mario_x + 2:
			for j in range(WIDTH):
				final_board[i] = arts.background[i]
		else:
			for j in range(WIDTH):
				if j < mario_y or j > mario_y + 6:
					final_board[i]+=arts.background[i][j]
				else:
					final_board[i]+=mario.art[i-mario_x][j-mario_y]
	for i in range(HEIGHT - 1):
		for j in range(WIDTH):
			print(final_board[i][j],end='')
		print()

class _Getch:

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException

_getch = _Getch()

def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = _getch()
        signal.alarm(0)	
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def rotate_background():
	for i in range(HEIGHT - 1):
		arts.background[i] = arts.background[i][1 : WIDTH] + arts.background[i][0]
		

RESET = True
HEIGHT = 29
WIDTH = 85
MAX_RIGHT = 45
mario = Mario(20,0,2)
background = []
small_mario = []
mario_character = []
brick = []
final_board = []
arts = Arts(background, small_mario, mario_character, brick, f)
arts.make_background()
arts.make_small_mario()
arts.make_mario()
arts.make_brick()
basic_background = arts.background
cur_time = time.time()
 
while RESET:
	if mario.life >= 2:
		mario.art = arts.mario_character
	else:
		mario.art = arts.small_mario
	# RESET = False
	os.system('tput reset')
	del final_board[:]
	printBoard(int(round(mario.x_pos)),int(round(mario.y_pos)))
	command = get_input()
	if command == 'q':
		break
	elif command == 'd':
		mario.move_right()
		if mario.y_pos == MAX_RIGHT:
			rotate_background()
			mario.distance_covered = mario.distance_covered + 1
	elif command == 'a':
		mario.move_left()
	elif command == 'w':
		mario.jump(arts.background)
	time_change = time.time() - cur_time
	mario.position_update(time_change,arts.background)
	cur_time = time.time()
