from tkinter import *


class OptionsComponent:

    def __init__(self, master, lifecycle, auto_lifecycle, stop_auto_lifecycle):
        frame = Frame(master)
        frame.pack()

        self.button_lifecycle = Button(master, text="update", width="15", command=lifecycle)
        self.button_auto_lifecycle = Button(master, text="Auto Update", width="15", command=auto_lifecycle)
        self.button_stop_auto_lifecycle = Button(master, text="Stop", width="15", command=stop_auto_lifecycle)
        self.label_generation = Label(master, text="Generation: 0")
        self.label_population = Label(master, text="Population: 0")

        self.button_lifecycle.pack()
        self.button_auto_lifecycle.pack()
        self.button_stop_auto_lifecycle.pack()
        self.label_generation.pack()
        self.label_population.pack()
