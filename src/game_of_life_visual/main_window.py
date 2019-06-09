import time
from tkinter import *

from src.game_of_life.Board import Board

root = Tk()
root.geometry("650x650")
root.title("Game of Life")
img = Image("photo", file="icon.png")
root.call('wm', 'iconphoto', root._w, img)

canvas_size = 600
grid_size_factor = 30

board = Board(int(canvas_size / grid_size_factor))

canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.config(background="white")

rectangles = []


def draw_grid(size: int, c: Canvas):
    for i in range(int(size / grid_size_factor)):
        c.create_line((i * grid_size_factor), 0, (i * grid_size_factor), size, width=1)
        for j in range(int(size / grid_size_factor)):
            c.create_line(0, (i * grid_size_factor), size, (i * grid_size_factor), width=1)


def click_rectangle(event):
    i = int(event.x / grid_size_factor)
    j = int(event.y / grid_size_factor)

    print("x: " + str(i) + " Y: " + str(j))

    if canvas.find_withtag(CURRENT):
        if canvas.itemcget(CURRENT, "fill") == "black":
            canvas.itemconfig(CURRENT, fill="white")
            board.board[i][j].alive = False
        else:
            canvas.itemconfig(CURRENT, fill="black")
            board.board[i][j].alive = True


def draw_rects(c: Canvas, size: int):
    for i in range(int(size / grid_size_factor)):
        rectangles.append([])
        for j in range(int(size / grid_size_factor)):
            x = (i * grid_size_factor)
            y = (j * grid_size_factor)
            color = "white"
            if board.board[i][j].alive:
                color = "black"
            rect = c.create_rectangle(x, y, (x + grid_size_factor), (y + grid_size_factor), fill=color,
                                      outline="white",
                                      tags="rectangle")
            rectangles[i].append(rect)


def test_rec_id():
    foo = rectangles[0][0]
    print(foo)
    if canvas.itemcget(foo, "fill") == "black":
        print("lol")
        canvas.itemconfig(foo, fill="white")
    else:
        canvas.itemconfig(foo, fill="black")
        print("lel")


def test_update():
    board.life_cycle()
    draw_rects(canvas, canvas_size)
    draw_grid(canvas_size, canvas)


button_start = Button(root, text="update", width="15", command=lambda: test_update())

input_x = Entry(root, width="5")
input_y = Entry(root, width="5")

canvas.grid(row=0, column=0, columnspan=3)
button_start.grid(row=1, column=2)

canvas.tag_bind("rectangle", "<Button-1>", click_rectangle)

draw_rects(canvas, canvas_size)
draw_grid(canvas_size, canvas)

root.mainloop()
