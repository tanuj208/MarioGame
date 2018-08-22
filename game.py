import sys, termios, tty, os, time, datetime, random, colorama as cl, numpy as np
import copy
from characters import *
from ascii import *
from input import *
import math

	
levelName = "temp"
RESET = True
HEIGHT = 29
SCREEN_WIDTH = 85
WIDTH = 510
MAX_RIGHT = 45
ENEMY_SPEED = 1   # seconds per block
ENEMY_LIFE = 1
arts = Arts()
arts.make_background(levelName)
arts.make_small_mario()
arts.make_mario()
arts.make_bumba()
mario = Mario(20, 0, 3, arts.mario_character)
cur_time = time.time()
enemies = []
f = open("enemies.txt",'r')
cnt = 0
for line in f.readlines():
	if cnt == 0:
		x = int(line)
	else:
		y = int(line)
		en = Enemy(x,y,ENEMY_LIFE,ENEMY_SPEED,1,arts.bumba)
		enemies.append(en)
	cnt = (cnt + 1) % 2
f.close()


def printBoard():
	final_board = copy.deepcopy(arts.background)
	for i in range(len(mario.art)):
		for j in range(len(mario.art[i]) - 1):
			final_board[int(round(mario.x_pos)) + i][int(round(mario.y_pos)) + j] = mario.art[i][j]

	for k in range(len(enemies)):
		for i in range(len(enemies[k].art)):
			for j in range(len(enemies[k].art[i]) - 1):
				final_board[enemies[k].x_pos + i][enemies[k].y_pos + j] = enemies[k].art[i][j]

	print("Score -> ",mario.score)
	print("Life -> ",mario.life)
	print("Chances -> ",mario.chances)
	for i in range(HEIGHT - 1):
		for j in range(SCREEN_WIDTH):
			print(final_board[i][j + mario.distance_covered],end='')
		print('')
	return final_board

while RESET:

	os.system('tput reset')
	if mario.life == 0:
		mario.chances -= 1
		mario.life = 3
		mario.x_pos = 20
		mario.y_pos = 0

	if mario.chances == 0:
		break

	if mario.life >= 2:
		mario.change_art(arts.mario_character)
	else:
		mario.change_art(arts.small_mario)
	# RESET = False
	final_board = printBoard()
	for i in range(len(enemies)):
		en = enemies[i]
		en.move(arts.background)
	command = get_input(0.1)
	if command == 'q':
		break
	elif command == 'd':
		mario.distance_covered = max(mario.distance_covered, mario.y_pos - MAX_RIGHT)
		mario.move_right(arts.background)
	elif command == 'a':
		mario.move_left(arts.background)
	elif command == 'w':
		mario.jump(arts.background)
	time_change = time.time() - cur_time
	mario.position_update(time_change,arts.background)
	mario.collision_check(enemies)
	cur_time = time.time()

print("Game Over")
