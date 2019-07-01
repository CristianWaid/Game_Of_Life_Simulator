from tkinter import *

from src.game_of_life_visual.main_window import MainWindow

root = Tk()
root.attributes('-fullscreen', True)
root.config(bg="white")
root.title("Game of Life")

game_of_life = MainWindow(root, 600, 10)

root.mainloop()
