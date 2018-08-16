import time

STANDARD_MOVE = 1
ACCEL = 10
GROUND_POS = 20
MAX_RIGHT = 45
MAX_LEFT = 0

class Character:
	def __init__(self,x,y,life):
		self.x_pos = x
		self.life = life
		self.y_pos = y
		self.vel = 0
		self.distance_covered = 0

	def move_right(self):
		self.y_pos = min(self.y_pos + STANDARD_MOVE, MAX_RIGHT)

	def move_left(self):
		self.y_pos = max(self.y_pos - STANDARD_MOVE, MAX_LEFT)

	def jump(self,final_board):
		if '_' in final_board[int(round(self.x_pos + 2))][int(round(self.y_pos)):int(round(self.y_pos + 7))] and self.vel >= 0:
			self.vel = -((6*ACCEL)) ** (1/2.0)

	def position_update(self,time_change,final_board):
		if '_' in final_board[int(round(self.x_pos + 2))][int(round(self.y_pos)):int(round(self.y_pos + 7))] and self.vel >= 0:
			self.vel = 0
		else:
			self.x_pos = self.x_pos + (self.vel * time_change) + (ACCEL * time_change * time_change * 0.5)
			self.vel = self.vel + ACCEL * time_change
		if self.x_pos >= GROUND_POS:
			self.x_pos = GROUND_POS
			self.vel = 0

class Mario(Character):
	def __init__(self, x, y, life):
		Character.__init__(self,x, y, life)
		self.score = 0
	def initialize_art(self, art):
		self.art = art