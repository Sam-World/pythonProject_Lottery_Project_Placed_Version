from random import randint, choice
from tkinter import *

# Constants
font = 'Britannic Bold'
size = '25'
background_colour = '#45CFDD'

# -------------- orange --- yellow --- green ---- blue ----- purple --- pink -- #
ball_colours = ["#FD8D14", "#FFC436", "#79AC78", "#279EFF", "#9D76C1", "#FF52A2"]


class RandNum:
    def __init__(self):
        self.lotto_numbers = []

        self.canvas = Canvas(width=750, height=100, background=background_colour, highlightthickness=0)
        self.canvas.place(x=50, y=500)

        self.draw_list = []
        self.random_lotto_number()

    def random_lotto_number(self):
        self.draw_list = []
        while len(self.draw_list) < 7:
            generate_ball_number = randint(1, 49)
            if generate_ball_number not in self.draw_list:
                self.draw_list.append(generate_ball_number)
                self.draw_list.sort()

    def clear_balls(self):
        self.canvas = Canvas(width=750, height=100, background=background_colour, highlightthickness=0)
        self.canvas.place(x=50, y=500)
        self.random_lotto_number()

    def get_balls(self):
        self.clear_balls()
        self.canvas.create_oval(100, 25, 155, 80, fill=choice(ball_colours)) # Outline= will set the ball outline colour
        self.canvas.create_text(128, 51, text=self.draw_list[0], fill="white", font=(font, size))
        self.canvas.after(1000, func=self.second_ball)

    def second_ball(self):
        self.canvas.create_oval(175, 25, 230, 80, fill=choice(ball_colours))
        self.canvas.create_text(202, 51, text=self.draw_list[1], fill="white", font=(font, size))
        self.canvas.after(1000, func=self.third_ball)

    def third_ball(self):
        self.canvas.create_oval(250, 25, 305, 80, fill=choice(ball_colours))
        self.canvas.create_text(277, 51, text=self.draw_list[2], fill="white", font=(font, size))
        self.canvas.after(1000, func=self.fourth_ball)

    def fourth_ball(self):
        self.canvas.create_oval(325, 25, 380, 80, fill=choice(ball_colours))
        self.canvas.create_text(353, 51, text=self.draw_list[3], fill="white", font=(font, size))
        self.canvas.after(1000, func=self.fifth_ball)

    def fifth_ball(self):
        self.canvas.create_oval(400, 25, 455, 80, fill=choice(ball_colours))
        self.canvas.create_text(428, 51, text=self.draw_list[4], fill="white", font=(font, size))
        self.canvas.after(1000, func=self.sixth_ball)

    def sixth_ball(self):
        self.canvas.create_oval(475, 25, 530, 80, fill=choice(ball_colours))
        self.canvas.create_text(502, 51, text=self.draw_list[5], fill="white", font=(font, size))
        self.canvas.after(1000, func=self.bonus_ball)

    def bonus_ball(self):
        is_in_list = True
        while is_in_list:
            bonus_num = randint(1, 49)
            if bonus_num not in self.draw_list:
                self.canvas.create_oval(600, 25, 655, 80, fill="#FE0000") # Bonus Ball - must be red
                self.canvas.create_text(627, 51, text=bonus_num, fill="white", font=(font, size))
                return bonus_num
