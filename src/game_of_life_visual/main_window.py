import time
from tkinter import *

from src.game_of_life.board import Board
from src.game_of_life_visual.options_component import OptionsComponent


class MainWindow:

    def __init__(self, master, canvas_size: int, grid_size_factor):
        frame = Frame(master)
        frame.grid()

        self.canvas_size = canvas_size
        self.grid_size_factor = grid_size_factor  # factor which changes board size(canvas_size/grid_size factor == board size)

        self.rectangles = []  # stores rectangle objects
        self.toggle_auto_update = False

        # current boars which is shown
        self.board = Board(int(self.canvas_size / self.grid_size_factor))

        self.canvas = Canvas(master, width=self.canvas_size, height=self.canvas_size, bd=0, highlightthickness=2,
                             relief=FLAT, highlightbackground="gray", background="white")

        self.canvas.place(x=100, y=50)

        # bind click_event for all rectangle canvas objects
        self.canvas.tag_bind("rectangle", "<Button-1>", self.handle_rectangle_click)

        # initialize the options component with the function handed through as event_listeners
        self.options = OptionsComponent(master, self.lifecycle, self.auto_lifecycle, self.stop_auto_lifecycle,
                                        self.change_board_size, self.reset_board)
        # draw the empty board to end init
        self.draw_rectangles()
        self.draw_grid()

    # draws board grid
    def draw_grid(self):
        for i in range(1, int(self.canvas_size / self.grid_size_factor)):
            self.canvas.create_line((i * self.grid_size_factor), 0, (i * self.grid_size_factor), self.canvas_size, width=1)
            for j in range(1, int(self.canvas_size / self.grid_size_factor)):
                self.canvas.create_line(0, (i * self.grid_size_factor), self.canvas_size, (i * self.grid_size_factor), width=1)

    # draw rectangles(white -> if cell is "dead", black -> if cell is "alive" && appends rectangle to rectangles list)
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

    # toggles the rectangles color and live status, counts population and updates labels
    def handle_rectangle_click(self, event):
        i = int(event.x / self.grid_size_factor)
        j = int(event.y / self.grid_size_factor)

        if self.canvas.find_withtag(CURRENT):
            if self.canvas.itemcget(CURRENT, "fill") == "black":
                self.canvas.itemconfig(CURRENT, fill="white")
                self.board.board[i][j].alive = False
                self.board.population -= 1
                self.options.update_label(self.board.population, self.board.generation)
            else:
                self.canvas.itemconfig(CURRENT, fill="black")
                self.board.board[i][j].alive = True
                self.board.population += 1
                self.options.update_label(self.board.population, self.board.generation)

    # updates the rectangles after simulation step
    def update_rectangles(self):
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles[i])):
                if self.board.board[i][j].alive:
                    self.canvas.itemconfig(self.rectangles[i][j], fill="black")
                else:
                    self.canvas.itemconfig(self.rectangles[i][j], fill="white")

    # simulates a whole lifecycle and updates the view
    def lifecycle(self):
        self.board.life_cycle()
        self.update_rectangles()
        self.options.update_label(self.board.population, self.board.generation)

    # auto simulates with given sleep time && stops if population == 0
    def auto_lifecycle(self):
        self.toggle_auto_update = True
        self.options.toggle_scale_view()
        while self.toggle_auto_update and self.board.population != 0:
            time.sleep(float(self.options.scale_update_sleep_time.get()))
            self.lifecycle()
            self.canvas.update_idletasks()
            self.canvas.update()
        self.options.toggle_scale_view()

    # stops auto simulation
    def stop_auto_lifecycle(self):
        self.toggle_auto_update = False

    # changes board size and resets board
    def change_board_size(self, grid_size_factor):
        self.grid_size_factor = self.options.get_board_size()
        self.board = Board(self.canvas_size // self.grid_size_factor)
        self.rectangles = []
        self.draw_rectangles()
        self.draw_grid()

    # resets board and all labels
    def reset_board(self):
        self.stop_auto_lifecycle()
        self.board = Board(int(self.canvas_size // self.grid_size_factor))
        self.rectangles = []
        self.draw_rectangles()
        self.draw_grid()
        self.options.update_label(self.board.population, self.board.generation)
