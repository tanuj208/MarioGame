import time

standard_move = 1
accel = 10
ground_pos = 20
max_right = 45
max_left = 0

class Character:
	def __init__(self,x,y,life):
		self.x_pos = x
		self.life = life
		self.y_pos = y
		self.vel = 0
		self.distance_covered = 0

	def move_right(self):
		self.y_pos = min(self.y_pos + standard_move, max_right)

	def move_left(self):
		self.y_pos = max(self.y_pos - standard_move, max_left)

	def jump(self):
		if self.x_pos < ground_pos:
			return
		self.vel = -((6*accel)) ** (1/2.0)

	def position_update(self,time_change):
		self.x_pos = self.x_pos + (self.vel * time_change) + (accel*time_change*time_change*0.5)
		self.vel = self.vel + accel * time_change
		if self.x_pos >= ground_pos:
			self.x_pos = ground_pos
			self.vel = 0

class Mario(Character):
	def __init__(self, x, y, life):
		Character.__init__(self,x, y, life)
	def initialize_art(self, art):
		self.art = art