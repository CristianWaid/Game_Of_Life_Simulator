import webbrowser
from tkinter import *


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

        self.scale_is_shown = True

        self.icon_button_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_next_line.png", width=25, height=25)
        self.icon_button_auto_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_play_line.png", width=25, height=25)
        self.icon_button_stop_auto_lifecycle = PhotoImage(file="src/game_of_life_visual/icons/button_pause_line.png", width=25, height=25)
        self.icon_button_information = PhotoImage(file="src/game_of_life_visual/icons/button_wikipedia.png", width=50, height=50)

        self.tk_var = StringVar(master)
        self.tk_var.set("60x60")

        self.button_lifecycle = Button(master, image=self.icon_button_lifecycle, bg="white", command=lifecycle, highlightthickness=0, bd=0)
        self.button_auto_lifecycle = Button(master, image=self.icon_button_auto_lifecycle, command=auto_lifecycle, highlightthickness=0, bd=0)
        self.button_stop_auto_lifecycle = Button(master, image=self.icon_button_stop_auto_lifecycle, command=stop_auto_lifecycle, highlightthickness=0, bd=0)
        self.button_reset = Button(master, text="reset", width="15", command=reset_board)
        self.button_set_board_size = Button(master, text="apply", command=lambda: change_board_size(20))
        self.button_information = Button(master, image=self.icon_button_information, command=self.open_wikipedia, highlightthickness=0, bd=0)
        self.scale_update_sleep_time = Scale(from_=0, to=2, orient=HORIZONTAL, resolution=0.1, font=("4", 10), length=130)
        self.label_generation = Label(master, text="Generation: 0")
        self.label_population = Label(master, text="Population: 0")
        self.label_sleep_time = Label(master, text="sleeptime (in sec.)", font=("4", 10))
        self.option_menu_board_size = OptionMenu(master, self.tk_var, *self.choices)

        self.scale_update_sleep_time.set(1)

        self.button_lifecycle.image = self.icon_button_lifecycle

        self.button_lifecycle.place(x=520, y=680)
        self.button_auto_lifecycle.place(x=460, y=680)
        self.button_stop_auto_lifecycle.place(x=490, y=680)
        self.button_reset.place(x=650, y=702.5, height=25, width=100)
        self.scale_update_sleep_time.place(x=438, y=710)
        self.label_generation.place(x=300, y=40)
        self.label_population.place(x=600, y=40)
        self.option_menu_board_size.place(x=250, y=680, height=25, width=100)
        self.button_set_board_size.place(x=250, y=710, height=25, width=100)
        self.button_information.place(x=945, y=715)
        self.label_sleep_time.place(x=455, y=750)

    def get_board_size(self):
        return self.choices.get(self.tk_var.get())

    @staticmethod
    def open_wikipedia():
        webbrowser.open("https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life")

    def toggle_scale_view(self):
        if self.scale_is_shown:
            self.scale_update_sleep_time.place_forget()
            self.label_sleep_time.place_forget()
            print("hide")
            self.scale_is_shown = False
        else:
            self.scale_update_sleep_time.place(x=438, y=710)
            self.label_sleep_time.place(x=455, y=750)
            print("show")
            self.scale_is_shown = True
