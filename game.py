import sys, termios, tty, os, time, datetime, random, colorama as cl, numpy as np
import copy
from characters import *
from ascii import *
from input import *
import math


f = open("b.txt",'r')

def printBoard():
	final_board = copy.deepcopy(arts.background)
	for i in range(len(mario.art)):
		for j in range(len(mario.art[i]) - 1):
			final_board[int(round(mario.x_pos)) + i][int(round(mario.y_pos)) + j + mario.distance_covered] = mario.art[i][j]

	for k in range(len(enemies)):
		for i in range(len(enemies[k].art)):
			for j in range(len(enemies[k].art[i]) - 1):
				final_board[enemies[k].x_pos + i][enemies[k].y_pos + j] = enemies[k].art[i][j]

	for i in range(HEIGHT - 1):
		for j in range(SCREEN_WIDTH):
			print(final_board[i][j + mario.distance_covered],end='')
		print('')
	return final_board

levelName = "b.txt"
RESET = True
HEIGHT = 29
SCREEN_WIDTH = 85
WIDTH = 510
MAX_RIGHT = 45
arts = Arts()
arts.make_background(levelName)
arts.make_small_mario()
arts.make_mario()
arts.make_bumba()
mario = Mario(20, 0, 2, arts.mario_character)
cur_time = time.time()
enemies = []
en = Enemy(22, 20, 1, 0.5, 1, arts.bumba)
enemies.append(en)

while RESET:
	if mario.life >= 2:
		mario.change_art(arts.mario_character)
	else:
		mario.change_art(arts.small_mario)
	# RESET = False
	os.system('tput reset')
	final_board = printBoard()
	for i in range(len(enemies)):
		en = enemies[i]
		en.move(arts.background)
	command = get_input(0.1)
	if command == 'q':
		break
	elif command == 'd':
		blocked = mario.move_right(arts.background)
		if not blocked and mario.y_pos == MAX_RIGHT:
			mario.distance_covered = mario.distance_covered + 1
	elif command == 'a':
		mario.move_left(arts.background)
	elif command == 'w':
		mario.jump(arts.background)
	time_change = time.time() - cur_time
	mario.position_update(time_change,arts.background)
	cur_time = time.time()
