import os
import copy
from input import *
import time

def openFile(filename, flag):

    while True:
        try:
            f = open(filename, flag)
            break
        except:
            filename = input("Please enter a valid level name\n")
            continue
    return f, filename

print("Choose\n1->Make new level\n2->Edit existing level\n")

while True:
    try:
        flag = int(input())
        break
    except:
        print("Enter an integer\n")

levelName = input("Enter level name\n")

if flag == 1:
    flag = 'w+'
else:
    flag = 'a'

if flag == 'a':
    f, levelName = openFile(levelName, 'r')
else:
    f = openFile("background.txt", 'r')[0]
background = []
HEIGHT = 28
WIDTH = 423
SCREEN_WIDTH = 85
MAX_RIGHT = 45
for i in range(HEIGHT):
    background.append(list(f.readline()))
f.close()

f = openFile(levelName + "enemies.txt", flag)[0]
if flag == 'w+':
    f.write('')
f.close()

f = openFile(levelName + "flyingEnemies.txt", flag)[0]
if flag == 'w+':
    f.write('')
f.close()

valid_inputs = ['b', 'p', 'g', 's', 'e', 'q', 'c', 'o', 'm', 'f']
direction_inputs = ['w', 'a', 's', 'd', 'q', 'm']

x_cor = 0
y_cor = 0

def superimpose(object_ascii, x, y):
    final_background = copy.deepcopy(background)
    for i in range(len(object_ascii)):
        for j in range(len(object_ascii[0]) - 1):
            final_background[i + x][j + y] = object_ascii[i][j]
    return final_background

def printBoard(board, y):
    for i in range(HEIGHT):
        for j in range(SCREEN_WIDTH):
            print(board[i][j + max(0, y - MAX_RIGHT)],end='')
        print('')

def get_ascii(filename):
    f = open(filename, 'r')
    object_ascii = []
    for line in f.readlines():
        object_ascii.append(list(line))
    return object_ascii


while True:
    os.system('tput reset')
    print("Input instructions\nb->brick p->pit g->ground object s->spring e->enemy f->flying enemy c->coin o->powerup q->save and quit m-> do not save and quit")
    printBoard(background, y_cor)
    try:
        x = get_input(1)
        if x not in valid_inputs:
            continue
    except:
        print("Read input instructions\n")
        time.sleep(1)
        continue

    if x == 'm':
        break

    if x == 'q':
        f = open(levelName, "w+")
        final = []
        for i in range(HEIGHT):
            final.append('')
            for j in range(WIDTH):
                final[i] += background[i][j]
            final[i] += '\n'
        for i in range(HEIGHT):
            f.write(final[i])
        f.close()
        break

    flag = 0
    object_ascii = []
    if x == 'b':
        object_ascii = get_ascii("brick.txt")
    elif x == 'p':
        object_ascii = get_ascii("pit.txt")
    elif x == 'g':
        object_ascii = get_ascii("groundObject.txt")
    elif x == 's':
        object_ascii = get_ascii("spring.txt")
    elif x == 'c':
        object_ascii = get_ascii("coin.txt")
    elif x == 'o':
        object_ascii = get_ascii("powerUp.txt")
    elif x == 'f':
        flag = 2
        object_ascii = get_ascii("flyingEnemy.txt")
    elif x == 'e':
        flag = 1
        object_ascii = get_ascii("enemy.txt")

    # x_cor = 0
    # y_cor = 0
    while True:
        os.system('tput reset')
        print("Input instructions\nw->move up a->move left s->move down d->move right q->save and quit m->do not save and quit")
        final_background = superimpose(object_ascii, x_cor, y_cor)
        printBoard(final_background, y_cor)
        try:
            y = get_input(1)
            if y not in direction_inputs:
                continue
        except:
            print("Read input instructions\n")
            time.sleep(1)
            continue
        if y == 'w':
            x_cor = max(x_cor - 1, 0)
        elif y == 'a':
            y_cor = max(y_cor - 1, 0)
        elif y == 's':
            x_cor = min(x_cor + 1, HEIGHT - len(object_ascii))
        elif y == 'd':
            y_cor = min(y_cor + 1, WIDTH - len(object_ascii[0]))    
        elif y == 'q':
            if flag == 1:
                f = open(levelName + "enemies.txt", 'a')
            elif flag == 2:
                f = open(levelName + "flyingEnemies.txt", 'a')
            if flag == 1 or flag == 2:
                f.write(str(x_cor)+'\n')
                f.write(str(y_cor)+'\n')
                f.close()
            else:
                background = final_background
            break
        elif y == 'm':
            break
