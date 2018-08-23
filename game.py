import sys, termios, tty, os, time, datetime, random
import copy
from characters import *
from ascii import *
from input import *
from missile import *
import math

LEVEL = 1
levelName = "level" + str(LEVEL)
RESET = True
HEIGHT = 29
SCREEN_WIDTH = 85
WIDTH = 423
MAX_RIGHT = 45
ENEMY_SPEED = 1 / LEVEL   # seconds per block
DRAGON_SPEED = ENEMY_SPEED / (1.5)
ENEMY_LIFE = LEVEL
DRAGON_LIFE = 10 * ENEMY_LIFE
DRAGON_JUMP = 10
MARIO_JUMP = 8
DRAGON_FIRE_SPEED = 5 / LEVEL # seconds per block
arts = Arts()
arts.make_background(levelName)
arts.make_small_mario()
arts.make_mario()
arts.make_enemy()
arts.make_flyingEnemy()
arts.make_missile()
arts.make_dragon()
arts.make_fire()
mario = Mario(20, 0, 1, arts.mario_character)
cur_time = time.time()
enemies = []
missiles = []

def takeCoordinates(fileName):
	f = open(fileName, 'r')
	cnt = 0
	for line in f.readlines():
		if cnt == 0:
			x = int(line)
		else:
			y = int(line)
			flying = 0
			art = arts.enemy
			if fileName == levelName + "enemies.txt":
				flying = 0
				art = arts.enemy
			else:
				flying = 1
				art = arts.flyingEnemy
			en = Enemy(x, y, ENEMY_LIFE, ENEMY_SPEED, 1, art, flying, 0, DRAGON_FIRE_SPEED)
			enemies.append(en)
		cnt = (cnt + 1) % 2
	f.close()

def superImpose():
	final_board = copy.deepcopy(arts.background)
	for i in range(len(mario.art)):
		for j in range(len(mario.art[i]) - 1):
			final_board[int(round(mario.x_pos)) + i][int(round(mario.y_pos)) + j] = mario.art[i][j]

	for k in range(len(enemies)):
		for i in range(len(enemies[k].art)):
			for j in range(len(enemies[k].art[i]) - 1):
				final_board[int(round(enemies[k].x_pos)) + i][int(round(enemies[k].y_pos)) + j] = enemies[k].art[i][j]

	for missile in missiles:
		final_board[missile.x_pos][missile.y_pos] = missile.art[0][0]
	return final_board

def printBoard(final_board):
	print("Score -> ",mario.score)
	print("Life -> ",mario.life)
	print("Chances -> ",mario.chances)
	if enemies[0].dragon == 0:
		print("Dragon Life -> 0")
	else:
		print("Dragon Life -> ",enemies[0].life)
	for i in range(HEIGHT - 1):
		for j in range(SCREEN_WIDTH):
			print(final_board[i][j + mario.distance_covered],end='')
		print('')

dragon = Enemy(16, 320, DRAGON_LIFE, DRAGON_SPEED, 1, arts.dragon, 0, 1, DRAGON_FIRE_SPEED)
enemies.append(dragon)
takeCoordinates(levelName + "enemies.txt")
takeCoordinates(levelName + "flyingEnemies.txt")
win = 0

while True:

	if mario.y_pos >= 375:
		win = 1
		break
	if mario.chances <= 0:
		break
	mario.changeForm(arts)

	final_board = superImpose()
	os.system('tput reset')
	print(mario.y_pos)
	printBoard(final_board)

	time_change = time.time() - cur_time
	i = -1
	for en in enemies:
		i += 1
		if en.life <= 0:
			mario.score += 10 / en.speed + 20 * en.max_life
			del enemies[i]
			continue
		if en.dragon == 1:
			if mario.x_pos < en.x_pos + 2:
				en.jump(arts.background, DRAGON_JUMP)
			if mario.y_pos < en.y_pos:
				en.move_to_left = 1
			else:
				en.move_to_left = 0
			launch_fire(missiles, arts, mario, en)
		en.move(arts.background)
		if en.flying == 0:
			en.position_update(time_change, arts.background)

	command = get_input(0.1)
	if command == 'q':
		break
	elif command == 'd':
		mario.move_right(arts.background)
		prev_distance = mario.distance_covered
		mario.distance_covered = max(mario.distance_covered, mario.y_pos - MAX_RIGHT)
		mario.score += mario.distance_covered - prev_distance
	elif command == 'a':
		mario.move_left(arts.background)
	elif command == 'w':
		mario.jump(arts.background, MARIO_JUMP)
	elif command == 'f':
		launch_missile(missiles, arts, mario)

	missile_status_check(final_board, missiles, enemies, mario)

	mario.position_update(time_change,arts.background)
	mario.collision_check(enemies, arts.background)
	mario.check_respawn()
	cur_time = time.time()

if win == 0:
	print("Game Over")
else:
	print("Level Completed")
print("Final Score ->",mario.score)
