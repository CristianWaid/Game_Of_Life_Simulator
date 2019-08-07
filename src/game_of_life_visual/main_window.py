import time
from tkinter import *

from src.game_of_life.board import Board
from src.game_of_life_visual.options_component import OptionsComponent


class MainWindow:
    def __init__(self, master, canvas_size: int, grid_size_factor):
        """
        represents main window of the Simulation
        :param master: master (or root) window, where the main window should be placed
        :param canvas_size: size of the Canvas(in pixel)
        :param grid_size_factor: factor which changes board size(canvas_size/grid_size factor == board size)
        """

        frame = Frame(master)
        frame.grid()

        self.canvas_size = canvas_size
        self.grid_size_factor = grid_size_factor

        self.rectangles = []  # stores rectangle objects
        self.toggle_auto_update = False

        # current board which is shown
        self.board = Board(int(self.canvas_size / self.grid_size_factor))

        self.canvas = Canvas(master, width=self.canvas_size, height=self.canvas_size, bd=0, highlightthickness=2,
                             relief=FLAT, highlightbackground="gray", background="white")
        # place canvas
        self.canvas.place(x=100, y=50)

        # bind click_event for all rectangle canvas objects
        self.canvas.tag_bind("rectangle", "<Button-1>", self.handle_rectangle_click)

        # initialize the options component with the function handed through as event_listeners
        self.options = OptionsComponent(master, self.lifecycle, self.auto_lifecycle, self.stop_auto_lifecycle,
                                        self.change_board_size, self.reset_board)
        # draw the empty board to end init
        self.draw_rectangles()
        self.draw_grid()

    def draw_grid(self):
        """
        draws the grid for the board.
        Note: grid should be drawn after the rectangles (otherwise grid isn't visible)
        :return: None
        """
        for i in range(1, int(self.canvas_size / self.grid_size_factor)):
            self.canvas.create_line((i * self.grid_size_factor), 0, (i * self.grid_size_factor), self.canvas_size, width=1)
            for j in range(1, int(self.canvas_size / self.grid_size_factor)):
                self.canvas.create_line(0, (i * self.grid_size_factor), self.canvas_size, (i * self.grid_size_factor), width=1)

    def draw_rectangles(self):
        """
        draw rectangles(white -> if cell is "dead", black -> if cell is "alive" && appends rectangle to rectangles list)
        :return: None
        """
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
        """
        toggles the rectangles color and live status, counts population and updates labels
        :param event: the current rectangle
        :return: None
        """
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

    def update_rectangles(self):
        """
        updates the rectangles after simulation step
        iterates through rectangles list (each rectangle is drawn "black" if: corresponding cell = Alive, otherwise rectangle color = "white")
        :return: None
        """
        for i in range(len(self.rectangles)):
            for j in range(len(self.rectangles[i])):
                if self.board.board[i][j].alive:
                    self.canvas.itemconfig(self.rectangles[i][j], fill="black")
                else:
                    self.canvas.itemconfig(self.rectangles[i][j], fill="white")

    def lifecycle(self):
        """
        simulates a whole lifecycle and updates the view
        :return: None
        """
        self.board.life_cycle()
        self.update_rectangles()
        self.options.update_label(self.board.population, self.board.generation)

    def auto_lifecycle(self):
        """
        auto simulates with given sleep time && stops if population == 0
        :return: None
        """
        if not self.toggle_auto_update:
            self.options.toggle_scale_view()
        self.toggle_auto_update = True
        while self.toggle_auto_update and self.board.population != 0:
            time.sleep(float(self.options.scale_update_sleep_time.get()))
            self.lifecycle()
            self.canvas.update_idletasks()
            self.canvas.update()
        self.options.toggle_scale_view()

    def stop_auto_lifecycle(self):
        """
        stops auto simulation
        :return: None
        """
        self.toggle_auto_update = False

    def change_board_size(self):
        """
        changes board size and resets board
        :return: None
        """
        self.grid_size_factor = self.options.get_board_size()
        self.board = Board(self.canvas_size // self.grid_size_factor)
        self.rectangles = []
        self.draw_rectangles()
        self.draw_grid()

    def reset_board(self):
        """
        resets board and population + generation labels
        :return: None
        """
        self.stop_auto_lifecycle()
        self.board = Board(int(self.canvas_size // self.grid_size_factor))
        self.rectangles = []
        self.draw_rectangles()
        self.draw_grid()
        self.options.update_label(self.board.population, self.board.generation)
