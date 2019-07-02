import time
from tkinter import *

from src.game_of_life.Board import Board
from src.game_of_life_visual.options_component import OptionsComponent


class MainWindow:

    def __init__(self, master, canvas_size: int, grid_size_factor):
        frame = Frame(master)
        frame.grid()

        self.canvas_size = canvas_size
        self.grid_size_factor = grid_size_factor

        self.rectangles = []
        self.toggle_auto_update = False

        self.board = Board(int(self.canvas_size / self.grid_size_factor))

        self.canvas = Canvas(master, width=self.canvas_size, height=self.canvas_size, bd=0, highlightthickness=2,
                             relief=FLAT, highlightbackground="gray", background="white")

        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.canvas.tag_bind("rectangle", "<Button-1>", self.handle_rectangle_click)

        self.options = OptionsComponent(master, self.lifecycle, self.auto_lifecycle, self.stop_auto_lifecycle,
                                        self.change_board_size, self.reset_board)

        self.draw_rectangles()
        self.draw_grid()

    def draw_grid(self):
        for i in range(1, int(self.canvas_size / self.grid_size_factor)):
            self.canvas.create_line((i * self.grid_size_factor), 0, (i * self.grid_size_factor), self.canvas_size, width=1)
            for j in range(1, int(self.canvas_size / self.grid_size_factor)):
                self.canvas.create_line(0, (i * self.grid_size_factor), self.canvas_size, (i * self.grid_size_factor), width=1)

    def draw_rectangles(self):
        for i in range(int(self.canvas_size / self.grid_size_factor)):
            self.rectangles.append([])
            for j in range(int(self.canvas_size / self.grid_size_factor)):
                x = (i * self.grid_size_factor)
                y = (j * self.grid_size_factor)
                color = "white"
                if self.board.board[i][j].alive:
                    color = "black"
                rect = self.canvas.create_rectangle(x, y, (x + self.grid_size_factor), (y + self.grid_size_factor),
                                                    fill=color,
                                                    outline="white",
                                                    tags="rectangle")
                self.rectangles[i].append(rect)

    def handle_rectangle_click(self, event):
        i = int(event.x / self.grid_size_factor)
        j = int(event.y / self.grid_size_factor)

        if self.canvas.find_withtag(CURRENT):
            if self.canvas.itemcget(CURRENT, "fill") == "black":
                self.canvas.itemconfig(CURRENT, fill="white")
                self.board.board[i][j].alive = False
                self.board.population -= 1
                self.update_label()
            else:
                self.canvas.itemconfig(CURRENT, fill="black")
                self.board.board[i][j].alive = True
                self.board.population += 1
                self.update_label()

    def update_rectangles(self):
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles[i])):
                if self.board.board[i][j].alive:
                    self.canvas.itemconfig(self.rectangles[i][j], fill="black")
                else:
                    self.canvas.itemconfig(self.rectangles[i][j], fill="white")

    def lifecycle(self):
        self.board.life_cycle()
        self.update_rectangles()
        self.update_label()

    def auto_lifecycle(self):
        self.toggle_auto_update = True
        self.options.scale_update_sleep_time.grid_forget()
        while self.toggle_auto_update and self.board.population != 0:
            time.sleep(float(self.options.scale_update_sleep_time.get()))
            self.lifecycle()
            self.canvas.update_idletasks()
            self.canvas.update()
        self.options.scale_update_sleep_time.grid(column=0, row=4)

    def stop_auto_lifecycle(self):
        self.toggle_auto_update = False

    def update_label(self):
        self.options.label_generation.config(text="Generation: " + str(self.board.generation))
        self.options.label_population.config(text="Population: " + str(self.board.population))

    def change_board_size(self, grid_size_factor):
        self.grid_size_factor = self.options.get_board_size()
        self.board = Board(self.canvas_size // self.grid_size_factor)
        self.rectangles = []
        self.draw_rectangles()
        self.draw_grid()

    def reset_board(self):
        self.stop_auto_lifecycle()
        self.board = Board(int(self.canvas_size // self.grid_size_factor))
        self.rectangles = []
        self.draw_rectangles()
        self.draw_grid()
        self.update_label()
