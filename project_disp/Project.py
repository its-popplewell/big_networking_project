import os
import pickle

class Project:
    def __init__(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y

        self.box_coors = []

        self.projects = [

        ]

    def draw(self):
        self.c.create_rectangle(
            self.x - 2, self.y - 2,
            self.x + 600 + 2, self.y + 400 + 2,
            fill="",
            outline="#999999",
            width=4
        )

        for i in range(3):
            x_val = self.x + 200 * i
            for j in range(4):
                y_val = self.y + 100 * j

                self.c.create_rectangle(
                    x_val, y_val,
                    x_val + 200, y_val + 100,
                    outline="#777777",
                    fill="#333333",
                    activefill="#555555"
                )

                self.c.create_text(
                    x_val + 100, y_val + 50,
                    text=self.projects[i * 4 + j],
                    font=("Affogato, Patronum", 24, "bold"),
                    fill="#999999",
                    activefill="#CCCCCC"
                )

                if len(self.box_coors) != 12:
                    self.box_coors.append((x_val, y_val, x_val + 200, y_val + 100))


    def update(self, project_names):
        format_proj_names = []
        for proj in project_names:
            proj_name = ""
            for l in proj:
                if l != "\n":
                    proj_name += l

            format_proj_names.append(proj_name)

        self.projects = format_proj_names


    def click(self, m_x, m_y):
        # m_x -= self.x
        # m_y -= self.y
        proj_name = ""
        for box_coor in self.box_coors:
            if box_coor[0] < m_x < box_coor[2] and box_coor[1] < m_y < box_coor[3]:
                proj_name = self.projects[self.box_coors.index(box_coor)]
                return proj_name
                    # cs.send(pickle.dumps(proj_name))
                    # message = ""
                    # while not message:
                    #     try:
                    #         message = cs.recv(2048)
                    #         if message:
                    #             decoded_msg = pickle.loads(message)
                    #
                    #             fout = open(".show_project.txt", "w")
                    #             fout.write(self.projects[self.box_coors.index(box_coor)])
                    #             fout.close()
                    #
                    #             os.system("open .show_project.txt")
                    #
                    #             break
                    #
                    #     except:
                    #         continue
