from tkinter import *

from src.game_of_life_visual.main_window import MainWindow

root = Tk()
root.geometry("800x750")

# sets program icon
icon = PhotoImage(file="src/game_of_life_visual/icons/icon.png")
root.tk.call("wm", "iconphoto", root._w, icon)

root.config(bg="white")
root.resizable(False, False)
root.title("Game of Life")

# initialize main window
game_of_life = MainWindow(root, 600, 10)

root.mainloop()
