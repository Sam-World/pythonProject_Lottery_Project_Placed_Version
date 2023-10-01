from tkinter import *
from generate_numbers import RandNum

# Constants
button_text_colour = 'white'
font = 'Britannic Bold'
disabled_button_colour = "#B4B4B3"
lucky_dip_colour = "#FF52A2"
spin_button_colour = "#FD8D14"


class CreateSpinner:
    def __init__(self):
        self.count = 0
        self.image_number = 0

        self.spinner_image_1 = PhotoImage(file="spinner 1.png")
        self.spinner_image_2 = PhotoImage(file="spinner 2.png")
        self.spinner_image_3 = PhotoImage(file="spinner 3.png")
        self.spinner_image_4 = PhotoImage(file="spinner 4.png")
        self.spinner_image_5 = PhotoImage(file="spinner 5.png")
        self.spinner_image_rest = PhotoImage(file="rest image.png")

        self.canvas = Canvas(width=350, height=350, background="white", highlightthickness=0)
        self.item = self.canvas.create_image(175, 175, image=self.spinner_image_rest)
        self.canvas.place(x=450, y=50)

    def spin_cage(self):
        self.clear_numbers()

        self.image_number += 1
        if self.image_number == 9:
            self.image_number = 1

        if self.image_number == 1:
            self.canvas.itemconfig(self.item, image=self.spinner_image_1)
        elif self.image_number == 2:
            self.canvas.itemconfig(self.item, image=self.spinner_image_2)
        elif self.image_number == 3:
            self.canvas.itemconfig(self.item, image=self.spinner_image_3)
        elif self.image_number == 4:
            self.canvas.itemconfig(self.item, image=self.spinner_image_4)
        elif self.image_number == 5:
            self.canvas.itemconfig(self.item, image=self.spinner_image_5)
        elif self.image_number == 6:
            self.canvas.itemconfig(self.item, image=self.spinner_image_4)
        elif self.image_number == 7:
            self.canvas.itemconfig(self.item, image=self.spinner_image_3)
        elif self.image_number == 8:
            self.canvas.itemconfig(self.item, image=self.spinner_image_2)
        if self.image_number == 9:
            self.canvas.itemconfig(self.item, image=self.spinner_image_1)

        self.count += 1
        if self.count < 24:
            self.canvas.after(200, self.spin_cage)
        else:
            self.canvas.itemconfig(self.item, image=self.spinner_image_rest)
            self.count = 0
            self.show_balls()

    def show_balls(self):
        random_number = RandNum()
        random_number.get_balls()

    def clear_numbers(self):
        clear_num = RandNum()
        clear_num.clear_balls()
