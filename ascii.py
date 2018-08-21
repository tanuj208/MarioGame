HEIGHT = 29
WIDTH = 85

class Arts:

	def __init__(self, background, small_mario, mario_character, bumba, f):
		self.background = background
		self.small_mario = small_mario
		self.mario_character = mario_character
		self.file = f
		self.bumba = bumba

	def make_background(self):
		for i in range(HEIGHT - 1):
			self.background.append(list(self.file.readline()))
	
	def make_small_mario(self):
		for i in range(3):
			self.small_mario.append(self.file.readline())

	def make_mario(self):
		for i in range(3):
			self.mario_character.append(self.file.readline())

	def make_bumba(self):
		f = open("bumba.txt", 'r')
		self.bumba.append(f.readline())
			