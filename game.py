import sys, termios, tty, os, time, datetime, random, colorama as cl, numpy as np

reset = True
# mario_character =
#     o
#  _ /<_
# (_)>(_)

standard_move = 4
height = 25
width = 75

board = np.full((25,75),'')

def printBoard():
	print ('\n'.join(''.join(str(cell) for cell in row) for row in board))

class Character:
	def __init__(self,x,y,life):
		self.x_pos = x
		self.life = life
		self.y_pos = y

	def move_right(self):
		self.x_pos = self.x_pos + standard_move

	def move_left(self):
		self.x_pos = self.x_pos - standard_move

	def jump(self):
		if self.y_pos <= 2 * standard_move:
			self.y_pos = self.y_pos + standard_move

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
while reset:
	reset = False
	os.system('tput reset')
	board[24]=np.full((1,75),'X')
	printBoard()
	command = getch()

