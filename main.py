import time_disp.Clock
import logo.Logo
import cash_box.Bank_Box as bb
import project_disp.Project as P
import tkinter as tk
import time
import socket
import pickle
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = socket.gethostbyname(socket.gethostname())
Port = 9999

client_socket.connect((IP_address, Port))
start_up = ""
while not start_up:
    try:
        message = client_socket.recv(2048)
        if message:
            decoded_msg = pickle.loads(message)
            start_up = decoded_msg

    except:
        continue


root = tk.Tk()
root.title("wtf am i doing")

clock_x = 200
clock_y = 0

date_font = ("Affogato, Patronum", 25, "bold")
projects_header = ("Affogato, Patronum", 90, "bold")
money_font = ("Affogato, Patronum", 60, "bold")

c = tk.Canvas(root, height=800, width=1200, bg="#383838", highlightthickness=0)
c.pack()

clock = time_disp.Clock.Clock(c, clock_x, clock_y)
logo = logo.Logo.Logo(c, 87.5, 87.5, 250)
bank_box = bb.Bank_Box(c, 700, 0)
bank_box.update(start_up[1][0], start_up[1][1])
p = P.Project(c, 40, 340)
p.update(start_up[0])

def update():
    c.delete("all")

    #draw and update the clock
    clock.update()
    clock.draw()

    #write the date
    c.create_text(clock_x + 200, clock_y + 155,
        text=time.strftime("%A, %B %d, %Y"),
        font=date_font,
        fill="#707070"
    )

    #draw the upper left square thingermaboob
    r = 25
    c.create_polygon(
        0, 0,
        0, 170,
        170 - r, 170,
        170 - r, 170 - r,
        170, 170 - r,
        170, 0,
        fill="#515151",
        outline=""
        )
    c.create_oval(125, 125, 170, 170, fill="#515151", outline="")

    #draw the logo / power off circle
    logo.draw()

    #Projects header
    c.create_text(335 , 265,
        text="PROJECTS",
        font=projects_header,
        fill="#C0C0C0",
        activefill="#FFFFFF"
    )

    #The big thing on the bottom right
    c.create_rectangle(700, 0, 1200, 800, fill="")
    c.create_rectangle(700, 225, 1200, 800, fill="#000000")


    #CASH BIT
    bank_box.draw()

    #Project Box
    # c.create_rectangle(40, 325, 640, 725, fill="", outline="#FFFFFF")
    p.draw()

    #950, 250
    c.create_oval(945, 245, 955, 255, outline="#656565", width=2) #selection bubble

    root.after(17, update)

update()

#if mouse in left corner, change to power off, otherwise leave it as the logo
def mouse_moved(event):
    if 0 < event.x < 170 and 0 < event.y < 170:
        logo.draw_symbols = [False, True]
    else:
        logo.draw_symbols = [True, False]

def mouse_clicked(event):
    if 0 < event.x < 170 and 0 < event.y < 170:
        root.quit()
        root.destroy()
    else:
        proj = p.click(event.x, event.y)
        if proj != "-------":
            output_msg = ("get_project", proj)
            client_socket.send(pickle.dumps(output_msg))
            message = ""
            while not message:
                try:
                    message = client_socket.recv(2048)
                    if message:
                        print("Message received")
                        decoded_msg = pickle.loads(message)
                        print(decoded_msg)

                        fout = open(".show_project.txt", "w")
                        fout.write(decoded_msg)
                        fout.close()

                        os.system("open .show_project.txt")
                        print("Project information displayed")

                        break

                except:
                    continue

root.bind("<Motion>", mouse_moved)
root.bind("<Button-1>", mouse_clicked)

root.mainloop()
client_socket.close()
