import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# This canvas is for the Tomato image with a size of 220 x 224
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png") # Read an image file to be added as arg in the canvas object
canvas.create_image(110, 112, image=tomato_png) # The width and height is half of the canvas so that my tomato will be hanging in the center of the canvas
canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()
