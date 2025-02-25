import tkinter as tk

root = tk.Tk()

radio_button = tk.Radiobutton(root, text='female', value=1).pack()
radio_button2 = tk.Radiobutton(root, text='male', value=2).pack()
root.mainloop()