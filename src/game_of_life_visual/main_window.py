from tkinter import *

root = Tk()
root.geometry("650x450")
root.title("Game of Life")
img = Image("photo", file="icon.png")
root.call('wm', 'iconphoto', root._w, img)

canvas_size = 600

canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.config(background="white")

rectangles = []


def test():
    print("foo")


def draw_rectangle(c: Canvas):
    x = int(input_x.get())
    y = int(input_y.get())
    c.create_rectangle(x, y, (x + 20), (y + 20), fill="black")


def draw_grid(x_max: int, y_max: int, c: Canvas):
    for i in range(int(x_max / 20)):
        c.create_line((i * 20), 0, (i * 20), y_max, width=1)
        for j in range(int(y_max / 20)):
            c.create_line(0, (i * 20), x_max, (i * 20), width=1)


def click_rectangle(event):
    print(event)
    if canvas.find_withtag(CURRENT):
        if canvas.itemcget(CURRENT, "fill") == "black":
            canvas.itemconfig(CURRENT, fill="white")
        else:
            canvas.itemconfig(CURRENT, fill="black")


def draw_rects(c: Canvas, size: int):
    for i in range(int(size / 20)):
        x = (i * 20)
        y = (i * 20)
        rect = c.create_rectangle(x, y, (x + 20), (y + 20), fill="black", tags="rectangle")
        rectangles.append(rect)
        for j in range(int(size / 20)):
            y = (j * 20)
            rect = c.create_rectangle(x, y, (x + 20), (y + 20), fill="black", tags="rectangle")
            rectangles.append(rect)


button_start = Button(root, text="test", width="15", command=lambda: draw_rectangle(canvas))

input_x = Entry(root, width="5")
input_y = Entry(root, width="5")

canvas.grid(row=0, column=0, columnspan=3)
input_x.grid(row=1, column=0)
input_y.grid(row=1, column=1)
button_start.grid(row=1, column=2)

canvas.tag_bind("rectangle", "<Button-1>", click_rectangle)

draw_grid(canvas_size, canvas_size, canvas)
draw_rects(canvas, canvas_size)

root.mainloop()
