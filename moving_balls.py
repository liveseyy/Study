from tkinter import *
from random import randint

width = 300
height = 200


class Ball:

    def __init__(self):
        self.R = randint(20, 50)
        self.x = randint(self.R, width - self.R)
        self.y = randint(self.R, height - self.R)
        self.dx, self.dy = 3, 2
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill='green')

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > width or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > height or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def main():
    global root, canvas, balls

    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    balls = [Ball() for ball in range(5)]

    tick()
    root.mainloop()


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


main()
