HEIGHT = 29
WIDTH = 85

class Arts:

	def __init__(self):
		self.background = []
		self.small_mario = []
		self.mario_character = []
		self.bumba = []

	def make_background(self, level):
		f = open(level, 'r')
		for i in range(HEIGHT - 1):
			self.background.append(list(f.readline()))
	
	def make_small_mario(self):
		f = open("small_mario.txt", 'r')
		for i in range(3):
			self.small_mario.append(f.readline())

	def make_mario(self):
		f = open("mario.txt", 'r')
		for i in range(3):
			self.mario_character.append(f.readline())

	def make_bumba(self):
		f = open("bumba.txt", 'r')
		self.bumba.append(f.readline())
			