import tkinter as tk

root = tk.Tk()
root.title('start the code')
button = tk.Button(root, text='STOP', width=25, command=root.destroy)
button.pack()

root.mainloop()