from tkinter import *
from tkinter import messagebox
from random import randint

# Constants
font = 'Britannic Bold'
size = '20'
ticket_colour = "#279EFF"
choose_numbers_colour = "#FF52A2"
button_text_colour = 'white'
spin_button_colour = "#FD8D14"
background_colour = '#45CFDD'


class Ticket:
    def __init__(self):
        self.player_list = []
        self.result = ""

        self.lotto_ticket_img = PhotoImage(file="lucky stars base resized.png")
        self.ticket_canvas = Canvas(width=350, height=350, background="white", highlightthickness=0)
        self.ticket_canvas.create_image(175, 175, image=self.lotto_ticket_img)
        self.ticket_canvas.place(x=50, y=50)

        self.pixel = PhotoImage(width=1, height=1)
        self.number_choice = Button(width=157, height=48, text="Choose Numbers", background=choose_numbers_colour,
                                    fg=button_text_colour, font=(font, 14), image=self.pixel, compound="center",
                                    command=self.choose_numbers)
        self.number_choice.place(x=233, y=425)

        self.number_selection = Entry(width=20, foreground="white", font=(font, 15), background=ticket_colour,
                                      highlightthickness=2)

    def clear_ticket(self):
        self.ticket_canvas = Canvas(width=350, height=350, background="white", highlightthickness=0)
        self.ticket_canvas.create_image(175, 175, image=self.lotto_ticket_img)
        self.ticket_canvas.place(x=50, y=50)

    def lucky_dip(self):
        self.clear_ticket()
        self.player_list = []
        self.number_choice.configure(text="Choose Numbers", background=choose_numbers_colour,
                                     command=self.choose_numbers)
        while len(self.player_list) < 6:
            generate_ticket_number = randint(1, 49)
            if generate_ticket_number not in self.player_list:
                self.player_list.append(generate_ticket_number)
                self.player_list.sort()
                self.result = str(self.player_list).strip('[]')
        self.ticket_canvas.create_text(172, 215, text=self.result, fill="white", font=(font, size))

    def choose_numbers(self):
        self.ticket_canvas.create_image(175, 175, image=self.lotto_ticket_img)

        # Example Text - Canvas
        example_canvas = Canvas(width=275, height=40, background=ticket_colour)
        example_canvas.create_text(140, 20, text="Example: 1, 2, 3, 4, 5, 6", font=(font, 15), fill="white")
        example_canvas.place(x=85, y=235)

        # Entry Box
        self.number_selection = Entry(width=20, foreground="white", font=(font, 15), background=ticket_colour,
                                      highlightthickness=2)
        self.number_selection.place(x=104, y=290)
        self.number_selection.focus()

        self.number_choice.configure(text="Check Numbers", background="#9D76C1", command=self.check_numbers)

    def check_numbers(self):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                   "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                   "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                   "41", "42", "43", "44", "45", "46", "47", "48", "49"
                   ]
        used_numbers = numbers
        choice = self.number_selection.get()
        li = list(choice.split(", "))

        if len(li) != 6:
            messagebox.showerror(title="Error", message="incorrect amount of numbers entered, please try again")
            self.number_selection.delete(0, END)
            return
        else:
            for num in range(len(li)):
                if li[num] in used_numbers:
                    used_numbers.remove(li[num])
                else:
                    messagebox.showerror(title="Error", message="invalid entry, please try again")
                    self.number_selection.delete(0, END)
                    return

        strip_list = [int(num) for num in li]
        strip_list.sort()
        final_numbers = str(strip_list).strip('[]')
        self.clear_ticket()
        self.ticket_canvas.create_text(172, 215, text=final_numbers, fill="white", font=(font, size))
        self.number_choice.configure(text="Choose Numbers", background=choose_numbers_colour,
                                     command=self.choose_numbers)

    def play_again(self):
        clear_ball_canvas = Canvas(width=750, height=100, background=background_colour, highlightthickness=0)
        clear_ball_canvas.place(x=50, y=500)
        self.number_choice.configure(text="Choose Numbers", background=choose_numbers_colour,
                                     command=self.choose_numbers)
        self.clear_ticket()
