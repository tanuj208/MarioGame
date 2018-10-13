import copy

HEIGHT = 29
SCREEN_WIDTH = 85
green = '\033[32m'
reset = '\033[39m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
bright = '\033[1m'
resetBright = '\033[22m'

class Board:

	def __init__(self, art):
		self.art = art

	def superImpose(self, mario, enemies, missiles):
		final_board = copy.deepcopy(self.art)
		for i in range(len(mario.art)):
			for j in range(len(mario.art[i]) - 1):
				if j == 0:
					final_board[int(round(mario.x_pos)) + i][int(round(mario.y_pos)) + j] = green + mario.art[i][j]
				elif j == len(mario.art[0]) - 2:
					final_board[int(round(mario.x_pos)) + i][int(round(mario.y_pos)) + j] = mario.art[i][j] + reset
				else:
					final_board[int(round(mario.x_pos)) + i][int(round(mario.y_pos)) + j] = mario.art[i][j]

		for k in range(len(enemies)):
			for i in range(len(enemies[k].art)):
				for j in range(len(enemies[k].art[i]) - 1):
					final_board[int(round(enemies[k].x_pos)) + i][int(round(enemies[k].y_pos)) + j] = enemies[k].art[i][j]

		for missile in missiles:
			final_board[missile.x_pos][missile.y_pos] = missile.art[0][0]
		return final_board

	def printBoard(self, final_board, mario, enemies):
		print("Score -> ",mario.score)
		print("Life -> ",mario.life)
		print("Chances -> ",mario.chances)
		if enemies[0].dragon == 0:
			print("Dragon Life -> 0")
		else:
			print("Dragon Life -> ",enemies[0].life)
		for i in range(HEIGHT - 1):
			for j in range(SCREEN_WIDTH):

				c = final_board[i][j + mario.distance_covered]
				if c == '|' or c == '_':
					final_board[i][j + mario.distance_covered] = red + c + reset
				elif c == '/' or c == '\\' or c == '{' or c == '}':
					final_board[i][j + mario.distance_covered] = yellow + c + reset
				elif c == '0':
					final_board[i][j + mario.distance_covered] = bright + magenta + c + reset + resetBright
				elif c == '$':
					final_board[i][j + mario.distance_covered] = bright + blue + c + reset + resetBright
				elif c == '~':
					final_board[i][j + mario.distance_covered] = green + c + reset

				print(final_board[i][j + mario.distance_covered],end = '')
			print('')
