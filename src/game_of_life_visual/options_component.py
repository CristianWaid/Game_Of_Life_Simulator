import webbrowser
from tkinter import *


def set_dark_mode(master):
    master.config(bg="black")


class OptionsComponent:

    def __init__(self, master, lifecycle, auto_lifecycle, stop_auto_lifecycle, change_board_size, reset_board):
        frame = Frame(master)
        frame.grid()

        self.choices = {'60x60': 10,
                        '40x40': 15,
                        "30x30": 20,
                        "20x20": 30,
                        "10x10": 60
                        }

        self.icon_button_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_next.png", width=25, height=25)
        self.icon_button_auto_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_play.png", width=25, height=25)
        self.icon_button_stop_auto_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_stop.png", width=25, height=25)
        self.icon_button_information = PhotoImage(file="src/game_of_life_visual/icons/button_wikipedia.png", width=50, height=50)

        self.tk_var = StringVar(master)
        self.tk_var.set("60x60")

        self.button_lifecycle = Button(master, image=self.icon_button_lifecycle, bg="white", command=lifecycle)
        self.button_auto_lifecycle = Button(master, image=self.icon_button_auto_lifecycle, command=auto_lifecycle)
        self.button_stop_auto_lifecycle = Button(master, image=self.icon_button_stop_auto_lifecycle, command=stop_auto_lifecycle)
        self.button_reset = Button(master, text="reset", width="15", command=reset_board)
        self.button_set_board_size = Button(master, text="set board size", command=lambda: change_board_size(20))
        self.button_dark_mode = Button(master, text="dark mode", command=lambda: set_dark_mode(master))
        self.button_information = Button(master, image=self.icon_button_information, command=self.open_wikipedia)
        self.scale_update_sleep_time = Scale(from_=0, to=2, orient=HORIZONTAL, label="sleep time (in sec)", length="135", resolution=0.1)
        self.label_generation = Label(master, text="Generation: 0")
        self.label_population = Label(master, text="Population: 0")
        self.option_menu_board_size = OptionMenu(master, self.tk_var, *self.choices)

        self.scale_update_sleep_time.set(1)

        self.button_lifecycle.image = self.icon_button_lifecycle

        self.button_lifecycle.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        self.button_auto_lifecycle.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        self.button_stop_auto_lifecycle.grid(column=0, row=2, sticky=W, padx=5, pady=5)
        self.button_reset.grid(column=0, row=3, sticky=W, padx=5, pady=5)
        self.scale_update_sleep_time.grid(column=0, row=4, sticky=W, padx=5, pady=5)
        self.label_generation.grid(column=0, row=5, sticky=W, padx=5, pady=5)
        self.label_population.grid(column=0, row=6, sticky=W, padx=5, pady=5)
        self.option_menu_board_size.grid(column=0, row=7, sticky=W, padx=5, pady=5)
        self.button_set_board_size.grid(column=0, row=8, sticky=W, padx=5, pady=5)
        self.button_dark_mode.grid(column=0, row=9, sticky=W, padx=5, pady=5)
        self.button_information.grid(column=0, row=10, sticky=W, padx=5, pady=5)

    def get_board_size(self):
        return self.choices.get(self.tk_var.get())

    @staticmethod
    def open_wikipedia():
        webbrowser.open("https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life")
