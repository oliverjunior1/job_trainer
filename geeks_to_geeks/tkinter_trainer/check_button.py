import tkinter as tk
from tkinter import Checkbutton, IntVar, mainloop

root = tk.Tk()
var1 = IntVar()
Checkbutton(root, text='male', variable=var1).grid(row=0)
var2 = IntVar()
Checkbutton(root, text='female', variable=var2).grid(row=1)
root.mainloop()