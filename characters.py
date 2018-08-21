import time

STANDARD_MOVE = 1
ACCEL = 10
GROUND_POS = 22
MAX_RIGHT = 45
MAX_LEFT = 0

class Character:
	def __init__(self,x,y,life, art):
		self.x_pos = x
		self.life = life
		self.y_pos = y
		self.vel = 0
		self.distance_covered = 0
		self.art = art

	def collision(self, final_background, x, y):
		for i in range(x, x + len(self.art) - 1):
			s = final_background[min(i, GROUND_POS)][y : min(y + len(self.art[0]) - 1, MAX_RIGHT + 10)]
			if '|' in s or '_' in s:
				return False
		s = final_background[min(x + len(self.art) - 1, GROUND_POS)][y : min(y + len(self.art[0]) - 1, MAX_RIGHT + 10)]
		if '|' in s:
			return False
		return True

	def move_right(self, final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if self.collision(final_background, rounded_x, rounded_y + STANDARD_MOVE):
			self.y_pos = min(self.y_pos + STANDARD_MOVE, MAX_RIGHT)
			return False
		return True

	def move_left(self, final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if self.collision(final_background, rounded_x, max(MAX_LEFT, rounded_y - STANDARD_MOVE)):
			self.y_pos = max(self.y_pos - STANDARD_MOVE, MAX_LEFT)

	def jump(self,final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if '_' in final_background[rounded_x + 2][rounded_y : rounded_y + 7] and self.vel >= 0:
			self.vel = -((6*ACCEL)) ** (1/2.0)

	def position_update(self,time_change,final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if '_' in final_background[rounded_x + 2][rounded_y : rounded_y + 7] and self.vel >= 0:
			self.vel = 0
		else:
			changed_x = int(round(self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)))
			if self.collision(final_background, changed_x, rounded_y):
				self.x_pos = self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)
				self.vel = self.vel + ACCEL * time_change
		if self.x_pos >= GROUND_POS:
			self.x_pos = GROUND_POS
			self.vel = 0

class Mario(Character):
	def __init__(self, x, y, life, art):
		Character.__init__(self, x, y, life, art)
		self.score = 0

	def change_art(self, art):
		self.art = art

class Enemy(Character):
	def __init__(self, x, y, life, speed, flag, art):
		Character.__init__(self, x, y, life, art)
		self.speed = speed
		# speed -> sec/block
		self.last_move = time.time()
		self.flag = flag
		# flag == 1 -> move to left
	def move(self, final_background):
		if time.time() - self.last_move >= self.speed:
			self.last_move = time.time()
			tmp_y = self.y_pos
			if self.flag == 1:
				self.move_left(final_background)
				if self.y_pos == tmp_y:
					self.flag = 0
					self.move_right(final_background)
			else:
				self.move_right(final_background)
				if self.y_pos == tmp_y:
					self.flag = 1
					self.move_left(final_background)
