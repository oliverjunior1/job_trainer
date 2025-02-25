import tkinter as tk
from tkinter import Listbox

root = tk.Tk()
lb = Listbox(root)
lb.insert(1, 'Rice')
lb.insert(2, 'Apple')
lb.insert(3, 'Bean')
lb.insert(4, 'Orange')
lb.pack()

root.mainloop()