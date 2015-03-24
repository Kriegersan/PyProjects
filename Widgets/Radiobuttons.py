__author__ = 'knelson'
from Tkinter import *

root = Tk()

v = IntVar()
v.set(1)

lang = [("Python", 1), ("Perl", 2), ("Java", 3), ("C++", 4), ("C", 5)]

def ShowChoice():
    print v.get()

Label(root, text="""Choose your favourite programming language""", justify =LEFT, padx=30).pack()

for txt, val in lang:
    Radiobutton(root, text=txt, indicatoron=0, width=30, padx=30, variable=v, command=ShowChoice, value=val).pack(anchor=W)

mainloop()

