from tkinter import *
from spin_cage import CreateSpinner
from generate_numbers import RandNum
from lucky_dip import Ticket

# Constants
font = 'Britannic Bold'
size = 14
lucky_dip_colour = "#FF52A2"
choose_numbers_colour = "#FF52A2"
spin_button_colour = "#FD8D14"
button_text_colour = 'white'
background_colour = '#45CFDD'
disabled_button_colour = "#B4B4B3"

# Create window
window = Tk()
window.configure(background=background_colour)
window.title("Lottery!")
window.geometry("850x750")

# Create Objects from Classes
spinner = CreateSpinner()
random_numbers = RandNum()
random_ticket_numbers = Ticket()

# Create Buttons
pixel = PhotoImage(width=1, height=1)
# Create image pixel of 1x1 to set the button size - now the button size won't change if the font size is increased

lucky_dip_button = Button(width=157, height=48, text="Lucky Dip", background=lucky_dip_colour,
                          fg=button_text_colour, font=(font, size), image=pixel, compound="center",
                          command=random_ticket_numbers.lucky_dip)
lucky_dip_button.place(x=50, y=425)

spin_button = Button(width=348, height=48, text="Spin", background=spin_button_colour, fg=button_text_colour,
                     image=pixel, compound="center", font=(font, size), command=spinner.spin_cage)
spin_button.place(x=450, y=425)

play_again_button = Button(width=745, height=76, background='yellow', text="Play Again!", font=(font, 20), image=pixel,
                           compound="center", command=random_ticket_numbers.play_again)
play_again_button.place(x=50, y=618)


window.mainloop()
