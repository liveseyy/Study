from tkinter import *
from random import randint

width = 300
height = 200


def main():
    global root, cvs
    global ball_id, R, x, y, dx, dy

    root = Tk()
    cvs = Canvas(root, width=width, height=height)
    cvs.pack()

    R = randint(20, 50)
    x = randint(R, width - R)
    y = randint(R, height - R)
    dx, dy = 3, 2
    ball_id = cvs.create_oval(x - R, y - R, x + R, y + R, fill='green')

    tick()
    root.mainloop()


def tick():
    global x, y, dx, dy
    x += dx
    y += dy
    cvs.move(ball_id, dx, dy)
    if x + R > width  or x - R <= 0:
        dx = -dx
    if y + R > height or y - R <= 0:
        dy = -dy
    root.after(50, tick)


main()

