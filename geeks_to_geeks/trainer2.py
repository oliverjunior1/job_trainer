import tkinter as tk
import random

root = tk.Tk()
root.geometry(('1300x200'))
def megasena():
    x = random.sample(range(1,61), 6)
    sorted(x)
    return label.config(text=f'The numbers of megasena are: {sorted(x)}')
def lotofacil():
    x = random.sample(range(1,25), 15)
    sorted(x)
    return label.config(text=f'The numbers of megasena are: {sorted(x)}')

label = tk.Label(root, text="João 14:13-14. Nessa passagem, Jesus diz que fará tudo o que for pedido em seu nome para que o Pai seja glorificado no Filho. A passagem também diz que aquele que crê em Jesus fará as obras que ele faz e fará ainda maiores do que essas")
label.pack()
button1 = tk.Button(root, text='Click here to megasena', command=megasena)
button1.pack()
button2 = tk.Button(root, text='Click here to megasena', command=lotofacil)
button2.pack()
tk.mainloop()