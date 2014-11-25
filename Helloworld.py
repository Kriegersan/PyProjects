from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "Hello World!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Exit"
        self.QUIT["fg"]   = "blue"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "right"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello Computer",
        self.hi_there["fg"] = "green"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()




root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
