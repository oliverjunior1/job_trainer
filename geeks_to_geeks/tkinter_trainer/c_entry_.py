import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='Name').pack()
Entry = tk.Entry().pack()
Button = tk.Button(root, text='send').pack()
root.mainloop()