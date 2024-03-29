import webbrowser
from tkinter import *


class OptionsComponent:

    def __init__(self, master, lifecycle, auto_lifecycle, stop_auto_lifecycle, change_board_size, reset_board):
        """
        manages all the options available in the Tkinter GUI
        :param master: master (or root) window, where the main window should be placed
        :param lifecycle: event_listener for lifecycle Button
        :param auto_lifecycle: event_listener for auto_lifecycle Button
        :param stop_auto_lifecycle: event_listener for stop_auto_lifecycle Button
        :param change_board_size: event_listener for apply_board_size
        :param reset_board: event_listener for reset_board Button
        """

        frame = Frame(master)
        frame.grid()

        # different sizes of board
        self.choices = {'60x60': 10,
                        '40x40': 15,
                        "30x30": 20,
                        "20x20": 30,
                        "10x10": 60
                        }

        # to toggle the visibility of scale component
        self.scale_is_shown = True

        # initialized all button icons
        self.icon_button_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_next_line.png", width=25, height=25)
        self.icon_button_auto_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_play_line.png", width=25, height=25)
        self.icon_button_stop_auto_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_pause_line.png", width=25, height=25)
        self.icon_button_information = PhotoImage(file="src/game_of_life_visual/icons/button_wikipedia.png", width=50, height=50)

        # set default option for diff. board sizes
        self.tk_var = StringVar(master)
        self.tk_var.set("60x60")

        # initialize buttons
        self.button_lifecycle = Button(master, image=self.icon_button_lifecycle, bg="white", command=lifecycle, highlightthickness=0, bd=0)
        self.button_auto_lifecycle = Button(master, image=self.icon_button_auto_lifecycle, command=auto_lifecycle, highlightthickness=0, bd=0)
        self.button_stop_auto_lifecycle = Button(master, image=self.icon_button_stop_auto_lifecycle, command=stop_auto_lifecycle, highlightthickness=0, bd=0)
        self.button_reset = Button(master, text="reset", command=reset_board, highlightthickness=0, bd=0)
        self.button_apply_board_size = Button(master, text="apply", command=lambda: change_board_size(), highlightthickness=0, bd=0)
        self.button_information = Button(master, image=self.icon_button_information, command=self.open_wikipedia, highlightthickness=0, bd=0)

        # initialize labels
        self.label_generation = Label(master, text="Generation: 0")
        self.label_population = Label(master, text="Population: 0")
        self.label_sleep_time = Label(master, text="sleeptime (in sec.)", font=("4", 10))

        # initialize OptionMenu
        self.option_menu_board_size = OptionMenu(master, self.tk_var, *self.choices)

        # initialize Scale
        self.scale_update_sleep_time = Scale(from_=0, to=2, orient=HORIZONTAL, resolution=0.1, font=("4", 10), length=130)

        # place all components
        self.button_lifecycle.place(x=420, y=660)
        self.button_auto_lifecycle.place(x=360, y=660)
        self.button_stop_auto_lifecycle.place(x=390, y=660)
        self.button_reset.place(x=550, y=690, height=25, width=100)
        self.button_apply_board_size.place(x=150, y=690, height=25, width=100)
        self.button_information.place(x=745, y=695)

        self.label_generation.place(x=200, y=20)
        self.label_population.place(x=500, y=20)
        self.label_sleep_time.place(x=355, y=730)

        self.scale_update_sleep_time.place(x=338, y=690)

        self.option_menu_board_size.place(x=150, y=660, height=25, width=100)

        self.scale_update_sleep_time.set(1)

    def get_board_size(self):
        """
        returns current selected board size from choices dictionary
        :return: selected board size (int)
        """
        return self.choices.get(self.tk_var.get())

    @staticmethod
    def open_wikipedia():
        """
        opens wikipedia in browser (for information)
        :return: None
        """
        webbrowser.open("https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life")

    def update_label(self, population: int, generation: int):
        """
        update the labels with given values
        :param population: value (int) to be shown in label_population
        :param generation: value (int) to be shown in generation
        :return: None
        """
        self.label_generation.config(text="Generation: " + str(generation))
        self.label_population.config(text="Population: " + str(population))

    def toggle_scale_view(self):
        """
        toggles visibility of scale and label_sleep_time (to avoid User to change sleep-time while auto simulate)
        :return: None
        """
        if self.scale_is_shown:
            self.scale_update_sleep_time.place_forget()
            self.label_sleep_time.place_forget()
            self.scale_is_shown = False
        else:
            self.scale_update_sleep_time.place(x=338, y=690)
            self.label_sleep_time.place(x=355, y=730)
            self.scale_is_shown = True
