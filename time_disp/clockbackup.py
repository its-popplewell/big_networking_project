import datetime

import tkinter as tk

class Clock:
    def __init__(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y

        self.blink = False
        self.hour = datetime.datetime.now().hour
        self.min = datetime.datetime.now().minute
        self.hourdraw = []
        self.mindraw = []

        self.DISPLAYS = {
            "0": "1110111",
            "1": "0110000",
            "2": "1101101",
            "3": "1111001",
            "4": "0110011",
            "5": "1011011",
            "6": "1011111",
            "7": "1110010",
            "8": "1111111",
            "9": "1110011"
        }

    def update(self):
        self.hour = str(datetime.datetime.now().hour % 12)
        self.min = str(datetime.datetime.now().minute)

        print(self.hour)

        if len(self.hour) == 1:
            self.hourdraw.append(self.DISPLAYS["0"])
        if len(self.min) == 1:
            self.mindraw.append(self.DISPLAYS["0"])

        for num in self.hour:
            self.hourdraw.append(self.DISPLAYS[num])
        for num in self.min:
            self.mindraw.append(self.DISPLAYS[num])

    def draw(self):
        #middle top -> bottom
        c.create_line(self.x + 50, self.x + 25, self.x + 87.5, self.x + 25, width=10)
        c.create_line(self.x + 50, self.x + 75, self.x + 87.5, self.x + 75, width=10)
        c.create_line(self.x + 50, self.x + 125, self.x + 87.5, self.x + 125, width=10)

        #left top -> bottom
        c.create_line(self.x + 43.75, self.x + 25 + 2, self.x + 43.75, self.x + 71.875, width=10)
        c.create_line(self.x + 43.75, self.x + 78.125, self.x + 43.75, self.x + 125 - 2, width=10)

        #right top -> bottom
        c.create_line(self.x + 93.75, self.x + 25 + 2, self.x + 93.75, self.x + 71.875, width=10)
        c.create_line(self.x + 93.75, self.x + 78.125, self.x + 93.75, self.x + 125 - 2, width=10)



        #middle top -> bottom
        c.create_line(self.x + 125,  self.x + 25, self.x + 162.5,  self.x + 25, width=10)
        c.create_line(self.x + 125, self.x + 75, self.x + 162.5, self.x + 75, width=10)
        c.create_line(self.x + 125, self.x + 125, self.x + 162.5, self.x + 125, width=10)

        #left top -> bottom
        c.create_line(self.x + 118.75,  self.x + 25 + 2, self.x + 118.75, self.x + 71.875, width=10)
        c.create_line(self.x + 118.75, self.x + 78.125, self.x + 118.75, self.x + 125 - 2, width=10)

        #right top -> bottom
        c.create_line(self.x + 168.75,  self.x + 25 + 2, self.x + 168.75, self.x + 71.875, width=10)
        c.create_line(self.x + 168.75, self.x + 78.125, self.x + 168.75, self.x + 125 - 2, width=10)

        #######

        #middle top -> bottom
        c.create_line(self.x + 237.5,  self.x + 25, self.x + 275,  self.x + 25, width=10)
        c.create_line(self.x + 237.5, self.x + 75, self.x + 275, self.x + 75, width=10)
        c.create_line(self.x + 237.5, self.x + 125, self.x + 275, self.x + 125, width=10)

        #left top -> bottom
        c.create_line(self.x + 231.25,  self.x + 25 + 2, self.x + 231.25, self.x + 71.875, width=10)
        c.create_line(self.x + 231.25, self.x + 78.125, self.x + 231.25, self.x + 125 - 2, width=10)

        #right top -> bottom
        c.create_line(self.x + 281.25,  self.x + 25 + 2, self.x + 281.25, self.x + 71.875, width=10)
        c.create_line(self.x + 281.25, self.x + 78.125, self.x + 281.25, self.x + 125 - 2, width=10)



        #middle top -> bottom
        c.create_line(self.x + 312.5,  self.x + 25, self.x + 350,  self.x + 25, width=10)
        c.create_line(self.x + 312.5, self.x + 75, self.x + 350, self.x + 75, width=10)
        c.create_line(self.x + 312.5, self.x + 125, self.x + 350, self.x + 125, width=10)

        #left top -> bottom
        c.create_line(self.x + 306.25,  self.x + 25 + 2, self.x + 306.25, self.x + 71.875, width=10)
        c.create_line(self.x + 306.25, self.x + 78.125, self.x + 306.25, self.x + 125 - 2, width=10)

        #right top -> bottom
        c.create_line(self.x + 356.25,  self.x + 25 + 2, self.x + 356.25, self.x + 71.875, width=10)
        c.create_line(self.x + 356.25, self.x + 78.125, self.x + 356.25, self.x + 125 - 2, width=10)


        #dots top -> bottom (300, 100), (300,150) as centers
        c.create_oval(self.x + 190, self.x + 40, self.x + 210, self.x + 60, fill="#000000")
        c.create_oval(self.x + 190, self.x + 90, self.x + 210, self.x + 110, fill="#000000")

root = tk.Tk()

c = tk.Canvas(root, height=600, width=600)
c.pack()

clock = Clock(c, 100, 50)

def update():
    c.delete('all')

    clock.update()
    clock.draw()

    root.after(17, update)

update()

root.mainloop()
