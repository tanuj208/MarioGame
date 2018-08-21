import os
import copy
from input import *

f = open("b.txt",'r')
background = []
HEIGHT = 28
WIDTH = 510
SCREEN_WIDTH = 85
MAX_RIGHT = 45
for i in range(HEIGHT):
    background.append(list(f.readline()))
f.close()

f = open("enemies.txt",'w+')
f.write('')
f.close()

valid_inputs = ['b', 'p', 'g', 's', 'e', 'q']
direction_inputs = ['w', 'a', 's', 'd', 'q']

x_cor = 0
y_cor = 0
flag = 0

def printt(object_ascii, x, y):
    final_background = copy.deepcopy(background)
    for i in range(len(object_ascii)):
        for j in range(len(object_ascii[0]) - 1):
            final_background[i + x][j + y] = object_ascii[i][j]
    for i in range(HEIGHT):
        for j in range(SCREEN_WIDTH):
            print(final_background[i][j + max(0, y - MAX_RIGHT)],end='')
        print('')
    return final_background

while True:
    os.system('tput reset')
    try:
        x = get_input(1)
        if x not in valid_inputs:
            continue
    except:
        continue

    if x == 'q':
        name = input()
        if flag == 1:
            f = open("enemies.txt",'a')
            f.write(str(x_cor)+'\n')
            f.write(str(y_cor)+'\n')
            f.close()
        f = open(name, "w+")
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

    object_ascii = []

    if x == 'b':
        flag = 0
        f = open("brick.txt", 'r')
        for i in range(2):
            object_ascii.append(list(f.readline()))
    elif x == 'p':
        flag = 0
        f = open("pit.txt", 'r')
        for i in range(3):
            object_ascii.append(list(f.readline()))
    elif x == 'g':
        flag = 0
        f = open("groundObject.txt", 'r')
        for i in range(3):
            object_ascii.append(list(f.readline()))
    elif x == 's':
        flag = 0
        f = open("spring.txt", 'r')
        object_ascii.append(list(f.readline()))
    elif x == 'e':
        flag = 1
        f = open("bumba.txt", 'r')
        object_ascii.append(list(f.readline()))

    x_cor = 0
    y_cor = 0
    print(object_ascii)
    while True:
        os.system('tput reset')
        final_background = printt(object_ascii, x_cor, y_cor)
        try:
            y = get_input(1)
            if y not in direction_inputs:
                continue
        except:
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
            background = final_background
            break
