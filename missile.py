import time
from characters import *

class Missile(Character):
    def __init__(self, x, y, speed, art, life):
        Character.__init__(self, x, y, life, art)
        self.speed = speed    # seconds per block
        self.last_move = time.time()

    def kill(self, enemies, background, mario):
        k = -1
        for en in enemies:
            k += 1
            enemy_x = int(round(en.x_pos))
            enemy_y = int(round(en.y_pos))
            if self.x_pos == enemy_x and self.y_pos >= enemy_y and self.y_pos < enemy_y + len(en.art[0]):
                mario.score += 10/en.speed
                del enemies[k]

    def move(self, background):
        last_y = self.y_pos
        if time.time() - self.last_move >= self.speed:
            self.last_move = time.time()
            self.move_right(background)
            if self.y_pos == last_y:
                self.life = 0
