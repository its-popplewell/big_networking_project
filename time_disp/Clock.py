import datetime

import tkinter as tk

class Clock:
    # 400 long, 150 high
    def __init__(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y

        self.blink = True
        # self.hour = str(datetime.datetime.now().hour
        # self.min = datetime.datetime.now().minute
        self.hourdraw = []
        self.mindraw = []

        # self.COLORS = ["#FFF1E4", "#842100"] for white bg
        self.COLORS = ["#404040", "#FF4000"]

        self.DISPLAYS = {
            "0": "1111110",
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
        self.hourdraw = []
        self.mindraw = []

        self.hour = datetime.datetime.now().hour
        if self.hour > 12:
            self.hour -= 12

        self.min = str(datetime.datetime.now().minute)
        self.hour = str(self.hour)

        if len(self.hour) == 1:
            self.hourdraw.append(self.DISPLAYS["0"])
        if len(self.min) == 1:
            self.mindraw.append(self.DISPLAYS["0"])

        for num in self.hour:
            self.hourdraw.append(self.DISPLAYS[num])
        for num in self.min:
            self.mindraw.append(self.DISPLAYS[num])

        if datetime.datetime.now().second % 2 == 0:
            self.blink = False
        else:
            self.blink = True

    def draw(self):

        # LEFT MOST
        # middle top, rights, middle bottom, lefts, middle middle
        # if self.hourdraw[0][0] == "1":
        self.c.create_line(self.x + 50, self.y + 25, self.x + 87.5, self.y + 25, width=10, fill=self.COLORS[int(self.hourdraw[0][0])])

        # if self.hourdraw[0][1] == "1":
        self.c.create_line(self.x + 93.75, self.y + 25 + 2, self.x + 93.75, self.y + 71.875, width=10, fill=self.COLORS[int(self.hourdraw[0][1])])

        # if self.hourdraw[0][2] == "1":
        self.c.create_line(self.x + 93.75, self.y + 78.125, self.x + 93.75, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.hourdraw[0][2])])

        # if self.hourdraw[0][3] == "1":
        self.c.create_line(self.x + 50, self.y + 125, self.x + 87.5, self.y + 125, width=10, fill=self.COLORS[int(self.hourdraw[0][3])])

        # if self.hourdraw[0][4] == "1":
        self.c.create_line(self.x + 43.75, self.y + 78.125, self.x + 43.75, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.hourdraw[0][4])])

        # if self.hourdraw[0][5] == "1":int(
        self.c.create_line(self.x + 43.75, self.y + 25 + 2, self.x + 43.75, self.y + 71.875, width=10, fill=self.COLORS[int(self.hourdraw[0][5])])

        # if self.hourdraw[0][6] == "1":
        self.c.create_line(self.x + 50, self.y + 75, self.x + 87.5, self.y + 75, width=10, fill=self.COLORS[int(self.hourdraw[0][6])])

#################################################

        # LEFT RIGHT
        # middle top, rights, middle bottom, lefts, middle middle
        # if self.hourdraw[1][0] == "1":
        self.c.create_line(self.x + 125,  self.y + 25, self.x + 162.5,  self.y + 25, width=10, fill=self.COLORS[int(self.hourdraw[1][0])])

        # if self.hourdraw[1][1] == "1":
        self.c.create_line(self.x + 168.75,  self.y + 25 + 2, self.x + 168.75, self.y + 71.875, width=10, fill=self.COLORS[int(self.hourdraw[1][1])])

        # if self.hourdraw[1][2] == "1":
        self.c.create_line(self.x + 168.75, self.y + 78.125, self.x + 168.75, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.hourdraw[1][2])])

        # if self.hourdraw[1][3] == "1":
        self.c.create_line(self.x + 125, self.y + 125, self.x + 162.5, self.y + 125, width=10, fill=self.COLORS[int(self.hourdraw[1][3])])

        # if self.hourdraw[1][4] == "1":
        self.c.create_line(self.x + 118.75, self.y + 78.125, self.x + 118.75, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.hourdraw[1][4])])

        # if self.hourdraw[1][5] == "1":
        self.c.create_line(self.x + 118.75,  self.y + 25 + 2, self.x + 118.75, self.y + 71.875, width=10, fill=self.COLORS[int(self.hourdraw[1][5])])

        # if self.hourdraw[1][6] == "1":
        self.c.create_line(self.x + 125, self.y + 75, self.x + 162.5, self.y + 75, width=10,  fill=self.COLORS[int(self.hourdraw[1][6])])

#########################################################

        # RIGHT LEFT
        # middle top, rights, middle bottom, lefts, middle middle
        # if self.mindraw[0][0] == "1":
        self.c.create_line(self.x + 237.5,  self.y + 25, self.x + 275,  self.y + 25, width=10, fill=self.COLORS[int(self.mindraw[0][0])])

        # if self.mindraw[0][1] == "1":
        self.c.create_line(self.x + 281.25,  self.y + 25 + 2, self.x + 281.25, self.y + 71.875, width=10, fill=self.COLORS[int(self.mindraw[0][1])])

        # if self.mindraw[0][2] == "1":
        self.c.create_line(self.x + 281.25, self.y + 78.125, self.x + 281.25, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.mindraw[0][2])])

        # if self.mindraw[0][3] == "1":
        self.c.create_line(self.x + 237.5, self.y + 125, self.x + 275, self.y + 125, width=10, fill=self.COLORS[int(self.mindraw[0][3])])

        # if self.mindraw[0][4] == "1":
        self.c.create_line(self.x + 231.25, self.y + 78.125, self.x + 231.25, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.mindraw[0][4])])

        # if self.mindraw[0][5] == "1":
        self.c.create_line(self.x + 231.25,  self.y + 25 + 2, self.x + 231.25, self.y + 71.875, width=10, fill=self.COLORS[int(self.mindraw[0][5])])

        # if self.mindraw[0][6] == "1":
        self.c.create_line(self.x + 237.5, self.y + 75, self.x + 275, self.y + 75, width=10, fill=self.COLORS[int(self.mindraw[0][6])])

######################################################

        # RIGHT MOST
        # middle top, rights, middle bottom, lefts, middle middle
        # if self.mindraw[1][0] == "1":
        self.c.create_line(self.x + 312.5,  self.y + 25, self.x + 350,  self.y + 25, width=10, fill=self.COLORS[int(self.mindraw[1][0])])

        # if self.mindraw[1][1] == "1":
        self.c.create_line(self.x + 356.25,  self.y + 25 + 2, self.x + 356.25, self.y + 71.875, width=10, fill=self.COLORS[int(self.mindraw[1][1])])

        # if self.mindraw[1][2] == "1":
        self.c.create_line(self.x + 356.25, self.y + 78.125, self.x + 356.25, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.mindraw[1][2])])

        # if self.mindraw[1][3] == "1":
        self.c.create_line(self.x + 312.5, self.y + 125, self.x + 350, self.y + 125, width=10, fill=self.COLORS[int(self.mindraw[1][3])])

        # if self.mindraw[1][4] == "1":
        self.c.create_line(self.x + 306.25, self.y + 78.125, self.x + 306.25, self.y + 125 - 2, width=10, fill=self.COLORS[int(self.mindraw[1][4])])

        # if self.mindraw[1][5] == "1":
        self.c.create_line(self.x + 306.25,  self.y + 25 + 2, self.x + 306.25, self.y + 71.875, width=10, fill=self.COLORS[int(self.mindraw[1][5])])

        # if self.mindraw[1][6] == "1":
        self.c.create_line(self.x + 312.5, self.y + 75, self.x + 350, self.y + 75, width=10, fill=self.COLORS[int(self.mindraw[1][6])])



###################################################

        #dots top -> bottom (300, 100), (300,150) as centers
        if self.blink:
            self.c.create_oval(self.x + 190, self.y + 40, self.x + 210, self.y + 60, fill=self.COLORS[1], outline="")
            self.c.create_oval(self.x + 190, self.y + 90, self.x + 210, self.y + 110, fill=self.COLORS[1], outline="")
