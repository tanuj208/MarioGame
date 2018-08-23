import time
from characters import *


def missile_status_check(final_board, missiles, enemies, mario):
    k = -1
    for missile in missiles:
        k += 1
        if missile.life == 0:
            del missiles[k]
        elif missile.fire == 0:
            missile.kill(enemies, final_board, mario)
        elif missile.fire == 1:
            missile.kill_mario(final_board, mario)

        missile.move(final_board)

def launch_missile(missiles, arts, mario):
    if mario.life == 3:
    	missiles.append(Missile(int(round(mario.x_pos)) + len(mario.art) - 1, int(round(mario.y_pos)) + len(mario.art[0]) - 1, 0.25, arts.missile, 1, 0, 0))

def launch_fire(missiles, arts, mario, dragon):
    if time.time() - dragon.last_fire < dragon.fire_speed:
        return
    
    dragon.last_fire = time.time()
    if mario.y_pos > dragon.y_pos:
        missiles.append(Missile(int(round(dragon.x_pos)) + 4, int(round(dragon.y_pos) + len(dragon.art[0])), 0.25, arts.fire, 1, 0, 1))
    else:
        missiles.append(Missile(int(round(dragon.x_pos)) + 4, int(round(dragon.y_pos)) - 1, 0.25, arts.fire, 1, 1, 1))

class Missile(Character):
    def __init__(self, x, y, speed, art, life, flag, fire):
        Character.__init__(self, x, y, life, art)
        self.speed = speed    # seconds per block
        self.last_move = time.time()
        self.move_to_left = flag
        self.fire = fire

    def kill(self, enemies, background, mario):
        k = -1
        for en in enemies:
            if self.life == 0:
                return
            k += 1
            enemy_x = int(round(en.x_pos))
            enemy_y = int(round(en.y_pos))
            if self.x_pos >= enemy_x and self.x_pos < enemy_x + len(en.art) and self.y_pos >= enemy_y and self.y_pos < enemy_y + len(en.art[0]):
                enemies[k].life -= 1
                self.life -= 1

    def move(self, background):
        last_y = self.y_pos
        if time.time() - self.last_move >= self.speed:
            self.last_move = time.time()
            if self.move_to_left == 0:
                self.move_right(background)
            else:
                self.move_left(background)
            if self.y_pos == last_y:
                self.life = 0
    
    def kill_mario(self, background, mario):
        if self.x_pos >= mario.x_pos and self.x_pos < mario.x_pos + len(mario.art) and self.y_pos >= mario.y_pos and self.y_pos < mario.y_pos + len(mario.art[0]):
            mario.life -= 1
            self.life -= 1
            return
