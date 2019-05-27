import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
counter = 0


def count():
    counter += 1


label = tk.Label(root, text="Test Window")
label.pack()

button = button = tk.Button(root, text='Stop', width=25, command=root.destroy, bg="blue")
button.pack()

root.mainloop()
