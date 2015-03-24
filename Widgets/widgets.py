__author__ = 'knelson'
from Tkinter import *

master = Tk()

weyd= "Whatever you do will be insignificant, but it is very important that you do it.\n (Mahatma Gandhi)"

msg = Message(master, text=weyd)
msg.config(bg='black', fg='green', font=('Times', 14, 'italic'))
msg.pack()

mainloop()
