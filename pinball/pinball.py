# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas


WIDTH, HEIGHT = 600, 400
INTERVAL = 90


ball = {
    'move_x': 15,
    'move_y': 15,
    'x': 350,
    'y': 300,
    'r': 10,
}


win = Tk()
win.title('pinball')
cv = Canvas(win, width = WIDTH, height = HEIGHT)
cv.pack()


def draw():
    cv.delete('all')
    cv.create_oval(
        ball['x'] - ball['r'],
        ball['y'] - ball['r'],
        ball['x'] + ball['r'],
        ball['y'] + ball['r'],
        fill = 'green'
    )


def move():
    xx = ball['x'] + ball['move_x']
    yy = ball['y'] + ball['move_y']

    if (xx < 0) or (xx > WIDTH):  ball['move_x'] *= -1
    if (yy < 0) or (yy > HEIGHT): ball['move_y'] *= -1

    if 0 <= xx <= WIDTH:  ball['x'] = xx
    if 0 <= yy <= HEIGHT: ball['y'] = yy

def pinball_loop():
    draw()
    move()
    win.after(INTERVAL, pinball_loop)


pinball_loop()
win.mainloop()
