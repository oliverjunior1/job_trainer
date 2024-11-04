from tkinter import *
from tkinter import ttk

root = Tk()
def callback():
    print('Your name:', entry.get())
    print('Your password:'+entry2.get())
    if chvar.get()==1:
        print('Remember me selected')
    else:
        print('not selected')

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry.insert(0,'Please enter your name')
entry2.insert(0,'Please enter your password')
button = ttk.Button(root, text='Enter')
lbltitle = ttk.Label(text='Our Title Here', font=(('Arial'),22))
lblname = ttk.Label(text='Your Name:')
lblpass = ttk.Label(text='Your Password:')
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=E, pady=5)
chvar=IntVar()
chvar.set(0)
cbox = Checkbutton(root, text='Remember me', variable=chvar, font='Arial 16').grid(row=4, column=0, sticky=E, columnspan=2)
button.config(command=callback)

root.geometry('500x450')
root.mainloop()