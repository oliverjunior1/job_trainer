from cProfile import label
from tkinter import *

from fontTools.mtiLib import build
from matplotlib.backend_bases import button_press_handler

root = Tk()

def callback():
    label.config(text='You clicked me!', fg='red', bg='yellow')

label = Label(root, text='Hello Python')
label.pack()
button= Button(root, text='Click Me', command=callback)
button.pack()
# button['state']= 'disabled'
# button['state']='enabled'

root.geometry('350x300')
root.mainloop()