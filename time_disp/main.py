import tkinter as tk
import time

from Clock import *

root = tk.Tk()

X_LOC = 0
Y_LOC = 0
SCALE = 1

font = ("Affogato, Patronum", 35, "bold")

c = tk.Canvas(root, height=600, width=600)
c.pack()

# clock_x = 300
# clock_y = 300
#
# clock = Clock(c, clock_x, clock_y)

def draw_date_and_time():
        clock.update()
        clock.draw()
        c.create_text(clock_x + 200, clock_y + 165, text=time.strftime("%A, %B %d, %Y"), font=font)

# def update():
#     c.delete("all")
#
#     draw_date_and_time()
#
#     root.after(17, update)
#
# update()
#
# root.mainloop()
