# import tkinter as tk
#
# root = tk.Tk()
#
# c = tk.Canvas(root, height=200, width=200, bg="#000000")
# c.pack()
#
# length = 200
# center_x = 100
# center_y = 100

class Logo:
    def __init__(self, c, x, y, length):
        self.c = c
        self.center_x = x
        self.center_y = y
        self.length = length

        self.draw_symbols = [True, False]

    def draw(self):
        if self.draw_symbols[0]:
            self.c.create_line(self.center_x - (self.length / 12), self.center_y - (self.length / 12) - 2, self.center_x - (self.length / 12), self.center_y, fill="#FF4000", width=4)
            self.c.create_line(self.center_x - (self.length / 12) - 2, self.center_y - (self.length / 12), self.center_x, self.center_y - (self.length / 12), fill="#FF4000", width=4)

            self.c.create_line(self.center_x + (self.length / 12), self.center_y, self.center_x + (self.length / 12), self.center_y + (self.length / 12) + 2, fill="#FF4000", width=4)
            self.c.create_line(self.center_x, self.center_y + (self.length / 12), self.center_x + (self.length / 12) + 2, self.center_y + (self.length / 12), fill="#FF4000", width=4)

            self.c.create_rectangle(self.center_x + (self.length/24), self.center_y - (self.length/8), self.center_x + (self.length/8), self.center_y - (self.length/24), fill="", outline="#FF4000", width=4)
            self.c.create_rectangle(self.center_x - (self.length/8), self.center_y + (self.length/24), self.center_x - (self.length/24), self.center_y + (self.length/8), fill="", outline="#FF4000", width=4)

            self.c.create_rectangle(self.center_x - (self.length/6), self.center_y + (self.length * (23/120)), self.center_x - (self.length/8), self.center_y + (self.length * (7/30)), fill="", outline="#FF4000", width=3)
            self.c.create_rectangle(self.center_x + (self.length/8), self.center_y - (self.length * (23/120)), self.center_x + (self.length/6), self.center_y - (self.length * (7/30)), fill= "", outline="#FF4000", width=3)

        elif self.draw_symbols[1]:
            self.c.create_oval(50, 50, 125, 125, outline="#FF4000", width=20)
            # self.c.create_polygon(
            #     20, 0,
            #     150, 0,
            #     85, 85,
            #     fill="#515151"
            #     )
            # self.c.create_line(85, 75, 85, 40, fill="#FF4000", width=4)
            # self.c.create_line(85, 75, 85, 40)

# def update():
#     c.delete("all")
#
#     # 1y1, 2x1: -2
#     c.create_line(center_x - (self.length / 12), center_y - (length / 12) - 2, center_x - (length / 12) , center_y, fill="#FF4000", width=4)
#     c.create_line(      center_x - (length / 12) - 2, center_y - (length / 12), center_x      , center_y - (length / 12), fill="#FF4000", width=4)
#
#     #1y2, 2x2 : +2
#     c.create_line(      center_x + (length / 12), center_y, center_x + (length / 12) , center_y + (length / 12) + 2, fill="#FF4000", width=4)
#     c.create_line(      center_x     , center_y + (length / 12), center_x + (length / 12) + 2, center_y + (length / 12), fill="#FF4000", width=4)
#
#     c.create_rectangle(center_x + (length/24) , center_y - (length/8), center_x + (length/8) , center_y - (length/24), fill="", outline="#FF4000", width=4)
#     c.create_rectangle(center_x - (length/8) , center_y + (length/24), center_x - (length/24) , center_y + (length/8), fill="", outline="#FF4000", width=4)
#
#     c.create_rectangle(center_x - (length/6), center_y + (length * (23/120)), center_x - (length/8) , center_y + (length * (7/30)), fill="", outline="#FF4000", width=4)
#     c.create_rectangle(center_x + (length/8) , center_y - (length * (23/120)), center_x + (length/6), center_y - (length * (7/30)), fill= "", outline="#FF4000", width=4)
#
#
#     # # 1y1, 2x1: -2
#     # c.create_line((5 / 12) * length, (5 / 12) * length - 2, (5 / 12) * length, (1 / 2) * length, fill="#FF4000", width=4)
#     # c.create_line((5 / 12) * length - 2, (5 / 12) * length, (1 / 2) * length, (5 / 12) * length, fill="#FF4000", width=4)
#     #
#     # #1y2, 2x2 : +2
#     # c.create_line((7 / 12) * length, (1 / 2) * length, (7 / 12) * length, (7 / 12) * length + 2, fill="#FF4000", width=4)
#     # c.create_line((1 / 2) * length, (7 / 12) * length, (7 / 12) * length + 2, (7 / 12) * length, fill="#FF4000", width=4)
#     #
#     # c.create_rectangle((13 / 24) * length, (3 / 8) * length, (5/8) * length, (11/24) * length, fill="", outline="#FF4000", width=4)
#     # c.create_rectangle((3 / 8) * length, (13 / 24) * length, (11/24) * length, (5/8) * length, fill="", outline="#FF4000", width=4)
#     #
#     # c.create_rectangle((1 / 3) * length, (83 / 120) * length, (3 / 8) * length, (11 / 15) * length, fill="", outline="#FF4000", width=4)
#
#
#
#     root.after(17, update)
#
# update()
#
# root.mainloop()
