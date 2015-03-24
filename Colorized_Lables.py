__author__ = 'knelson'
from Tkinter import *

root = Tk()

Label(root, text="Red Text in Times!", fg="red", font="Times").pack()

Label(root, text="Green on Green text Bold", fg="light green", bg="Dark Green", font="Times 18 bold").pack()

Label(root, text="blue with Helvetica", fg="blue", bg="light yellow", font="Helvetica 14 italic").pack()

Label(root, text="Verdana Bold", fg="green", bg="black", font="Verdana 12 bold").pack()


root.mainloop()

