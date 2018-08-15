
background = []
mario_character = []
height = 30
width = 85

class Objects:

	def __init__(self, background, mario_character, f):
		self.background = background
		self.mario_character = mario_character
		self.file = f

	def make_background(self):
		for i in range(height - 1):
			self.background.append(self.file.readline())

	def make_mario(self):
		for i in range(3):
			self.mario_character.append(self.file.readline())
