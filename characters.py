import time

STANDARD_MOVE = 1
ACCEL = 30
GROUND_POS = 22
MAX_RIGHT = 45
WIDTH = 423
COIN_SCORE = 10

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
			s = final_background[min(i, GROUND_POS)][y : y + len(self.art[0]) - 1]
			if '|' in s or '_' in s or '~' in s:
				return True
		s = final_background[min(x + len(self.art) - 1, GROUND_POS)][y : y + len(self.art[0]) - 1]
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

	def jump(self,final_background, jump_distance):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))

		s = final_background[rounded_x + len(self.art) - 1][rounded_y : rounded_y + len(self.art[0]) - 1]
		s1 = final_background[rounded_x + len(self.art)][rounded_y : rounded_y + len(self.art[0]) - 1]
		if ('_' in s or '~' in s or '`' in s1 or '|' in s1) and self.vel >= 0:
			self.vel = -((2*jump_distance*ACCEL)) ** (1/2.0)


	def position_update(self,time_change,final_background):
		rounded_x=int(round(self.x_pos))
		rounded_y=int(round(self.y_pos))
		s = final_background[rounded_x + len(self.art) - 1][rounded_y : rounded_y + len(self.art[0]) - 1]
		if '~' in s and self.vel >= 0:
			self.vel = -1.2 * self.vel
		elif ('_' in s or '`' in s) and self.vel >= 0:
			self.vel = 0
		else:
			changed_x = int(round(self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)))
			if changed_x <= 0:
				changed_x = 0
			if not self.collision(final_background, changed_x, rounded_y):
				self.x_pos = self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)
				if self.x_pos < 0:
					self.x_pos = 0
					self.vel = 0
				self.vel = self.vel + ACCEL * time_change
			else:
				self.vel = 0
		if self.x_pos + len(self.art) - 1 > GROUND_POS and final_background[27][rounded_y - 1 : rounded_y + len(self.art[0]) - 2].count('-') != len(self.art[0]) - 1:
			self.x_pos = GROUND_POS + 1 - len(self.art)
			rounded_x = int(round(self.x_pos))
			s = final_background[rounded_x + len(self.art) - 1][rounded_y : rounded_y + len(self.art[0]) - 1]
			if '~' in s and self.vel >= 0:
				self.vel = -1.2 * self.vel
			else:
				self.vel = 0

class Mario(Character):
	def __init__(self, x, y, life, art):
		Character.__init__(self, x, y, life, art)
		self.score = 0
		self.chances = 3

	def change_art(self, art):
		self.art = art

	def collision_check(self, enemies, background):
		rounded_x = int(round(self.x_pos))
		rounded_y = int(round(self.y_pos))

		if self.x_pos >= 25:
			self.life = 0
			return
		for i in range(len(self.art)):
			for j in range(len(self.art[0])):
				if background[rounded_x + i][rounded_y + j] == '0':
					self.score += COIN_SCORE
					background[rounded_x + i][rounded_y + j] = ' '
				elif background[rounded_x + i][rounded_y + j] == '$':
					self.life = min(self.life + 1, 3)
					self.score += COIN_SCORE
					background[rounded_x + i][rounded_y + j] = ' '
		k = -1
		for en in enemies:
			k += 1
			broke = 0
			enemy_x = int(round(en.x_pos))
			enemy_y = int(round(en.y_pos))
			for i in range(len(en.art)):
				for j in range(len(en.art[0])):
					if enemy_y + i < rounded_y + len(self.art[0]) and enemy_y + i >= rounded_y:
						if enemy_x + j >= rounded_x and enemy_x + j < rounded_x + len(self.art):
							if en.dragon == 1:
								self.life = 0
								return
							self.life -= 1
							del enemies[k]
							broke = 1
							break
						elif enemy_x == rounded_x + len(self.art):
							if en.flying == 1:
								self.score += 20/en.speed + 20 * en.max_life
							else:
								self.score += 10/en.speed + 20 * en.max_life
							del enemies[k]
							broke = 1
							break
				if broke == 1:
					break

	def changeForm(self, arts):
		if self.life >= 2:
			self.change_art(arts.mario_character)
		else:
			self.change_art(arts.small_mario)

	def check_respawn(self):
		if self.life == 0:
			self.chances -= 1
			self.life = 1
			self.x_pos = 20
			self.y_pos = 0
			self.score -= self.distance_covered
			self.distance_covered = 0

class Enemy(Character):
	def __init__(self, x, y, life, speed, move_to_left, art, flying, dragon, fire_speed):
		Character.__init__(self, x, y, life, art)
		self.speed = speed
		# speed -> sec/block
		self.last_move = time.time()
		self.move_to_left = move_to_left
		self.flying = flying
		self.dragon = dragon
		self.max_life = life
		self.last_fire = time.time()
		self.fire_speed = fire_speed

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
