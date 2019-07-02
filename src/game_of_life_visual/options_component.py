from tkinter import *


class OptionsComponent:

    def __init__(self, master, lifecycle, auto_lifecycle, stop_auto_lifecycle, change_board_size, reset_board):
        frame = Frame(master)
        frame.grid()

        self.choices = {'60x60': 10,
                        '40x40': 25,
                        "30x30": 20,
                        "20x20": 30,
                        "10x10": 60
                        }  # 10=50x50, 20=25x25 (500)
        self.tk_var = StringVar(master)
        self.tk_var.set("60x60")

        self.button_lifecycle = Button(master, text="update", width="15", command=lifecycle)
        self.button_auto_lifecycle = Button(master, text="Auto Update", width="15", command=auto_lifecycle)
        self.button_stop_auto_lifecycle = Button(master, text="Stop", width="15", command=stop_auto_lifecycle)
        self.button_reset = Button(master, text="reset", width="15", command=reset_board)
        self.scale_update_sleep_time = Scale(from_=0, to=2, orient=HORIZONTAL, label="sleep time (in sec)",
                                             length="150",
                                             resolution=0.1)
        self.label_generation = Label(master, text="Generation: 0")
        self.label_population = Label(master, text="Population: 0")
        self.option_menu_board_size = OptionMenu(master, self.tk_var, *self.choices)
        self.button_test = Button(master, text="set board size", command=lambda: change_board_size(20))

        self.scale_update_sleep_time.set(10)

        self.button_lifecycle.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        self.button_auto_lifecycle.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        self.button_stop_auto_lifecycle.grid(column=0, row=2, sticky=W, padx=5, pady=5)
        self.button_reset.grid(column=0, row=3, sticky=W, padx=5, pady=5)
        self.scale_update_sleep_time.grid(column=0, row=4, sticky=W, padx=5, pady=5)
        self.label_generation.grid(column=0, row=5, sticky=W, padx=5, pady=5)
        self.label_population.grid(column=0, row=6, sticky=W, padx=5, pady=5)
        self.option_menu_board_size.grid(column=0, row=7, sticky=W, padx=5, pady=5)
        self.button_test.grid(column=0, row=8, sticky=W, padx=5, pady=5)

    def get_board_size(self):
        return self.choices.get(self.tk_var.get())
