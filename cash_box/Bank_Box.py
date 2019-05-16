class Bank_Box:
    def __init__(self, c, x, y):
        self.x = x
        self.y = y
        self.c = c

        self.total = ""

        self.in_and_outs = [
            "-------",
            "-------",
            "-------",
            "-------",
            "-------"  #count = 7
        ]

        self.in_and_out_colors = ["#007705", "#BB0000", "#000000"]

    def draw(self):
        self.c.create_rectangle(
            self.x, self.y,
            self.x + 500, self.y + 225,
            fill="#C0C0C0",
            outline=""
        )

        self.c.create_line(
            self.x + 350, self.y,
            self.x + 350, self.y + 225,
        )

        self.total_amount = self.c.create_text(
            self.x + 175, self.y + 112.5,
            text=f"${self.total}",
            font=("Affogato, Patronum", 60, "bold")
        )

        for i in range(5):
            self.c.create_rectangle(
                self.x + 350, (i * 45) + self.y,
                self.x + 500, ((i + 1) * 45) + self.y,
                outline="",
                fill="#999999"
            )

            if self.in_and_outs[i] != "-------":
                if self.in_and_outs[i][0] == "-":
                    color = self.in_and_out_colors[1]
                else:
                    color = self.in_and_out_colors[0]
            else:
                color = self.in_and_out_colors[2]

            amt = self.in_and_outs[i]

            self.c.create_text(
                self.x + 425, ((i * 45) + self.y) + 22.5,
                text=amt,
                font=("Affogato, Patronum", 24, "bold"),
                fill=color
            )

    def update(self, total, changes):
        self.total = total[:-1]
        self.in_and_outs = changes

        for i in range(len(self.in_and_outs)):
            change = self.in_and_outs[i]
            self.in_and_outs[i] = change[:-1]
