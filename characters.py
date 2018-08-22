import time

STANDARD_MOVE = 1
ACCEL = 10
GROUND_POS = 22
MAX_RIGHT = 45
WIDTH = 510

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
				return True
		s = final_background[min(x + len(self.art) - 1, GROUND_POS)][y : min(y + len(self.art[0]) - 1, MAX_RIGHT + 10)]
		if '|' in s:
			return True
		return False

	def move_right(self, final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if not self.collision(final_background, rounded_x, rounded_y + STANDARD_MOVE):
			self.y_pos = min(self.y_pos + STANDARD_MOVE, WIDTH)

	def move_left(self, final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if not self.collision(final_background, rounded_x, max(self.distance_covered, rounded_y - STANDARD_MOVE)):
			self.y_pos = max(self.y_pos - STANDARD_MOVE, self.distance_covered)

	def jump(self,final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		if '_' in final_background[rounded_x + len(self.art) - 1][rounded_y : rounded_y + len(self.art[0]) - 1] and self.vel >= 0:
			self.vel = -((10*ACCEL)) ** (1/2.0)

	def position_update(self,time_change,final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		print(rounded_x, rounded_y)
		# print(final_background[rounded_x + len(self.art) - 1][rounded_y : rounded_y + len(self.art[0]) - 1])
		if '_' in final_background[rounded_x + len(self.art) - 1][rounded_y : rounded_y + len(self.art[0]) - 1] and self.vel >= 0:
			self.vel = 0
		else:
			changed_x = int(round(self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)))
			if not self.collision(final_background, changed_x, rounded_y):
				self.x_pos = self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)
				self.vel = self.vel + ACCEL * time_change
		if self.x_pos >= GROUND_POS:
			self.x_pos = GROUND_POS
			self.vel = 0

class Mario(Character):
	def __init__(self, x, y, life, art):
		Character.__init__(self, x, y, life, art)
		self.score = 0
		self.chances = 3

	def change_art(self, art):
		self.art = art

	def collision_check(self, enemies):
		k = -1
		rounded_x = int(round(self.x_pos))
		rounded_y = int(round(self.y_pos))
		for en in enemies:
			k += 1
			enemy_x = int(round(en.x_pos))
			enemy_y = int(round(en.y_pos))
			for i in range(len(en.art[0])):
				if enemy_y + i < rounded_y + len(self.art[0]) and enemy_y + i >= rounded_y:
					if enemy_x >= rounded_x and enemy_x < rounded_x + len(self.art):
						self.life -= 1
						del enemies[k]
						break
					elif enemy_x == rounded_x + len(self.art):
						self.score += 10/en.speed
						del enemies[k]
						break

class Enemy(Character):
	def __init__(self, x, y, life, speed, move_to_left, art):
		Character.__init__(self, x, y, life, art)
		self.speed = speed
		# speed -> sec/block
		self.last_move = time.time()
		self.move_to_left = move_to_left
	def move(self, final_background):
		if time.time() - self.last_move >= self.speed:
			self.last_move = time.time()
			tmp_y = self.y_pos
			if self.move_to_left == 1:
				self.move_left(final_background)
				if self.y_pos == tmp_y:
					self.move_to_left = 0
					self.move_right(final_background)
			else:
				self.move_right(final_background)
				if self.y_pos == tmp_y:
					self.move_to_left = 1
					self.move_left(final_background)
