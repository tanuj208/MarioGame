HEIGHT = 29
WIDTH = 85

class Arts:

	def __init__(self):
		self.background = []
		self.small_mario = []
		self.mario_character = []
		self.enemy = []
		self.missile = []

	def make_background(self, level):
		f = open(level, 'r')
		for line in f.readlines():
			self.background.append(list(line))
	
	def make_small_mario(self):
		f = open("small_mario.txt", 'r')
		for line in f.readlines():
			self.small_mario.append(line)

	def make_mario(self):
		f = open("mario.txt", 'r')
		for line in f.readlines():
			self.mario_character.append(line)

	def make_enemy(self):
		f = open("enemy.txt", 'r')
		for line in f.readlines():
			self.enemy.append(line)
			
	def make_missile(self):
		f = open("missile.txt", 'r')
		for line in f.readlines():
			self.missile.append(line)