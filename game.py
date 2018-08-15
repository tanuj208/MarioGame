import sys, termios, tty, os, time, datetime, random, colorama as cl, numpy as np
from characters import *
from ascii import *
import math


f = open("background.txt",'r')

def printt(mario_x,mario_y):
	for i in range(height-1):
		if i < mario_x or i > mario_x + 2:
			for j in range(width):
				print(objects.background[i][j],end='')
			print('')
		else:
			for j in range(width):
				if j < mario_y or j > mario_y + 6:
					print(objects.background[i][j],end='')
				else:
					print(mario.art[i-mario_x][j-mario_y],end='')
			print('')

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
	for i in range(height - 1):
		objects.background[i] = objects.background[i][1 : width] + objects.background[i][0]
		

reset = True
height = 29
width = 85
mario = Mario(20,0,2)
max_right = 45
background = []
small_mario = []
mario_character = []
brick = []
objects = Objects(background, small_mario, mario_character, brick, f)
objects.make_background()
objects.make_small_mario()
objects.make_mario()
objects.make_brick()
cur_time = time.time()
 
while reset:
	if mario.life >= 2:
		mario.art = objects.mario_character
	else:
		mario.art = objects.small_mario
	# reset = False
	os.system('tput reset')
	printt(int(round(mario.x_pos)),int(round(mario.y_pos)))
	command = get_input()
	if command == 'q':
		break
	elif command == 'd':
		mario.move_right()
		if mario.y_pos == max_right:
			rotate_background()
			mario.distance_covered = mario.distance_covered + 1
	elif command == 'a':
		mario.move_left()
	elif command == 'w':
		mario.jump()
	time_change = time.time() - cur_time
	mario.position_update(time_change)
	cur_time = time.time()
