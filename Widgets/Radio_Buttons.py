__author__ = 'knelson'
from Tkinter import *

root = Tk()

v = IntVar()

Label(root, text="""Choose a Programming language""", justify = LEFT, padx = 40).pack()

Radiobutton(root, text="Python", padx=40, variable=v, value=1).pack(anchor=W)

Radiobutton(root, text="Perl", padx=40, variable=v, value=2).pack(anchor=W)


mainloop()




