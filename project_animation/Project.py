class Project:
    def __init__(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y

        self.projects = [
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date"),
            ("Title", "Date")
        ]

    def draw(self):
        self.c.create_polygon(
            self.x + 25, self.y,
            self.x + 575, self.y,
            self.x + 575, self.y + 25,
            self.x + 600, self.y + 25,
            self.x + 600, self.y + 375,
            self.x + 575, self.y + 375,
            self.x + 575, self.y + 400,
            self.x + 25, self.y  + 400,
            self.x + 25, self.y + 375,
            self.x, self.y + 375,
            self.x, self.y + 25,
            self.x + 25, self.y + 25,
            outline="",
            fill="#999999"
        )

        self.c.create_oval(
            self.x, self.y,
            self.x + 50, self.y + 50,
            outline="",
            fill="#999999"
        )

        self.c.create_oval(
            self.x + 550, self.y,
            self.x + 600, self.y + 50,
            outline="",
            fill="#999999"
        )

        self.c.create_oval(
            self.x, self.y + 350,
            self.x + 50, self.y + 400,
            outline="",
            fill="#999999"
        )

        self.c.create_oval(
            self.x + 550, self.y + 350,
            self.x +600, self.y + 400,
            outline="",
            fill="#999999"
        )
