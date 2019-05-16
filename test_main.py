import project_disp.Project as P
import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, height=800, width=800, bg="#383838")
c.pack()

p = P.Project(c, 100, 200)

def update():
    c.delete("all")

    p.draw()

    root.after(17, update)

update()



root.mainloop()
