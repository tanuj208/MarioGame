import sys, termios, tty, os, time, datetime, random, colorama as cl, numpy as np
from characters import *
from ascii import *
from input import *
import math


f = open("background.txt",'r')

def printBoard(mario_x,mario_y):
	final_board = []
	for i in range(HEIGHT-1):
		final_board.append(arts.background[i])
	# 	if i < mario_x or i > mario_x + 2:
	# 		for j in range(WIDTH):
	# 			final_board[i] = arts.background[i]
	# 	else:
	# 		for j in range(WIDTH):
	# 			if j < mario_y or j > mario_y + 6:
	# 				final_board[i]+=arts.background[i][j]	
	# 			else:
	# 				final_board[i]+=mario.art[i-mario_x][j-mario_y]
	# final = []
	for i in range(len(mario.art)):
		for j in range(len(mario.art[i])):
			final_board[mario_x + i][mario_y + j] = mario.art[i][j]

	for i in range(HEIGHT - 1):
		final.append(list(final_board[i]))
	
	for i in range(HEIGHT - 1):
		for j in range(WIDTH):
			if enemies[0].x_pos == i and (enemies[0].y_pos == j or enemies[0].y_pos == j - 1 or enemies[0].y_pos == j - 2 or enemies[0].y_pos == j - 3):
				final[i][j] = enemies[0].art[0][j - enemies[0].y_pos]
	for i in range(HEIGHT - 1):
		for j in range(WIDTH):
			print(final[i][j],end='')
		print('')
	return final_board

def rotate_background():
	for i in range(HEIGHT - 1):
		arts.background[i] = arts.background[i][1 : WIDTH] + arts.background[i][0]
		
RESET = True
HEIGHT = 29
WIDTH = 85
MAX_RIGHT = 45
background = []
small_mario = []
mario_character = []
bumba = []
arts = Arts(background, small_mario, mario_character, bumba, f)
arts.make_background()
arts.make_small_mario()
arts.make_mario()
arts.make_bumba()
mario = Mario(20, 0, 2, arts.mario_character)
cur_time = time.time()
enemies = []
# en = Enemy(22, 20, 1, 1, 1, arts.bumba)
# enemies.append(en)

while RESET:
	if mario.life >= 2:
		mario.change_art(arts.mario_character)
	else:
		mario.change_art(arts.small_mario)
	# RESET = False
	os.system('tput reset')
	final_board = printBoard(int(round(mario.x_pos)),int(round(mario.y_pos)))
	for i in range(len(enemies)):
		en = enemies[i]
		en.move(arts.background)
	command = get_input(0.1)
	if command == 'q':
		break
	elif command == 'd':
		blocked = mario.move_right(arts.background)
		if not blocked and mario.y_pos == MAX_RIGHT:
			rotate_background()
			mario.distance_covered = mario.distance_covered + 1
	elif command == 'a':
		mario.move_left(arts.background)
	elif command == 'w':
		mario.jump(arts.background)
	time_change = time.time() - cur_time
	mario.position_update(time_change,arts.background)
	cur_time = time.time()
