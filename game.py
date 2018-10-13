import sys, termios, tty, os, time, datetime, random
import copy
from characters import *
from ascii import *
from input import *
from missile import *
from board import *
import math

while True:
	try:
		LEVEL = int(input("Choose difficulty(in integer)\n"))
		if LEVEL <= 0:
			print("use positive numbers\n")
		break
	except:
		print("Choose integer\n")

while True:
	try:
		flag = int(input("1. Choose your own level\nor Use existing levels\n"))
		break
	except:
		print("Input only integer\n")

levelName = ''

if flag != 1:
	levelName = "level" + str(LEVEL)
else:
	while True:
		try:
			levelName = input()
			f = open(levelName, 'r')
			f.close()
			break
		except:
			print("Enter valid level\n")

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
arts.make_background(levelName)
DRAGON_FIRE_SPEED = 5 / LEVEL # seconds per block
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
			if fileName == "enemyCoordinates/" + levelName + "enemies.txt":
				flying = 0
				art = arts.enemy
			else:
				flying = 1
				art = arts.flyingEnemy
			en = Enemy(x, y, ENEMY_LIFE, ENEMY_SPEED, 1, art, flying, 0, DRAGON_FIRE_SPEED)
			enemies.append(en)
		cnt = (cnt + 1) % 2
	f.close()

dragon = Enemy(16, 320, DRAGON_LIFE, DRAGON_SPEED, 1, arts.dragon, 0, 1, DRAGON_FIRE_SPEED)
enemies.append(dragon)
takeCoordinates("enemyCoordinates/" + levelName + "enemies.txt")
takeCoordinates("enemyCoordinates/" + levelName + "flyingEnemies.txt")
win = 0
board = Board(arts.background)

while True:

	if mario.y_pos >= 375:
		win = 1
		break
	if mario.chances <= 0:
		break
	mario.changeForm(arts)

	final_board = board.superImpose(mario, enemies, missiles)
	os.system('tput reset')
	print(mario.y_pos)
	board.printBoard(final_board, mario, enemies)

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
				en.jump(board.art, DRAGON_JUMP)
			if mario.y_pos < en.y_pos:
				en.move_to_left = 1
			else:
				en.move_to_left = 0
			launch_fire(missiles, arts, mario, en)
		en.move(board.art)
		if en.flying == 0:
			en.position_update(time_change, board.art)

	command = get_input(0.1)
	if command == 'q':
		break
	elif command == 'd':
		mario.move_right(board.art)
		prev_distance = mario.distance_covered
		mario.distance_covered = max(mario.distance_covered, mario.y_pos - MAX_RIGHT)
		mario.score += mario.distance_covered - prev_distance
	elif command == 'a':
		mario.move_left(board.art)
	elif command == 'w':
		mario.jump(board.art, MARIO_JUMP)
	elif command == 'f':
		launch_missile(missiles, arts, mario)

	missile_status_check(final_board, missiles, enemies, mario)

	mario.position_update(time_change,board.art)
	mario.collision_check(enemies, board.art)
	mario.check_respawn()
	cur_time = time.time()

if win == 0:
	print("Game Over")
else:
	print("Level Completed")
print("Final Score ->",mario.score)
