# -*- coding: utf-8 -*-

from random import randint
from tkinter import Tk, Canvas


COLS, ROWS = 60, 40
CW = 10
INTERVAL = 300
stage = []
for y in range(0, ROWS):
    stage.append([(randint(0, 4) == 0) for x in range(0, COLS)])


win = Tk()
win.title('life game')
cv = Canvas(win, width = (COLS * CW), height = (ROWS * CW))
cv.pack()


def check(x, y):
    cnt = 0
    tbl = [(-1, -1), (0, -1), (1, -1), (1, 0),
           (1, 1), (0, 1), (-1, 1), (-1, 0)]
    for t in tbl:
        xx, yy = x + t[0], y + t[1]
        if (0 <= xx < COLS) and (0 <= yy < ROWS):
            if stage[yy][xx]: cnt += 1

    if stage[y][x]:
        if 2 <= cnt <= 3: return True
        return False
    else:
        if cnt == 3: return True
    return stage[y][x]


def next_turn():
    global stage
    stage_tmp = []
    for y in range(0, ROWS):
        stage_tmp.append([check(x, y) for x in range(0, COLS)])
    stage = stage_tmp


def draw_stage():
    cv.delete('all')
    for y in range(0, ROWS):
        for x in range(0, COLS):
            if not stage[y][x]: continue
            xx, yy = x * CW, y * CW
            cv.create_oval(xx, yy, xx + CW, yy + CW, fill='red', width=0)


def game_loop():
    next_turn()
    draw_stage()
    win.after(INTERVAL, game_loop)


game_loop()
win.mainloop()
