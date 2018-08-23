HEIGHT = 29
WIDTH = 85

def read(filename):
	f = open(filename, 'r')
	ascii_list = []
	for line in f.readlines():
		ascii_list.append(line)
	return ascii_list

class Arts:

	def __init__(self):
		self.background = []

	def make_background(self, level):
		f = open(level, 'r')
		for line in f.readlines():
			self.background.append(list(line))
	
	def make_small_mario(self):
		self.small_mario = read("small_mario.txt")

	def make_mario(self):
		self.mario_character = read("mario.txt")

	def make_flyingEnemy(self):
		self.flyingEnemy = read("flyingEnemy.txt")

	def make_enemy(self):
		self.enemy = read("enemy.txt")
			
	def make_dragon(self):
		self.dragon = read("dragon.txt")

	def make_missile(self):
		self.missile = read("missile.txt")

	def make_fire(self):
		self.fire = read("fire.txt")
