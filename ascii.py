height = 29
width = 85

class Objects:

	def __init__(self, background, small_mario, mario_character, brick, f):
		self.background = background
		self.small_mario = small_mario
		self.mario_character = mario_character
		self.file = f
		self.brick = brick

	def make_background(self):
		for i in range(height - 1):
			self.background.append(self.file.readline())
	
	def make_small_mario(self):
		for i in range(3):
			self.small_mario.append(self.file.readline())

	def make_mario(self):
		for i in range(3):
			self.mario_character.append(self.file.readline())

	def make_brick(self):
		for i in range(2):
			self.brick.append(self.file.readline())
			