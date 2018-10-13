
def read(filename):
	f = open(filename, 'r')
	ascii_list = []
	for line in f.readlines():
		ascii_list.append(line)
	return ascii_list

class Arts:

	def __init__(self):
		self.background = []
		self.small_mario = read("ascii/small_mario.txt")
		self.mario_character = read("ascii/mario.txt")
		self.flyingEnemy = read("ascii/flyingEnemy.txt")
		self.enemy = read("ascii/enemy.txt")
		self.dragon = read("ascii/dragon.txt")
		self.missile = read("ascii/missile.txt")
		self.fire = read("ascii/fire.txt")
		self.coin = read("ascii/coin.txt")
		self.brick = read("ascii/brick.txt")
		self.groundObject = read("ascii/groundObject.txt")
		self.pit = read("ascii/pit.txt")
		self.powerUp = read("ascii/powerUp.txt")
		self.spring = read("ascii/spring.txt")

	def make_background(self, level):
		f = open(level, 'r')
		for line in f.readlines():
			self.background.append(list(line))
	
arts = Arts()
