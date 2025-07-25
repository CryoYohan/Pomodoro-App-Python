from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#28282B"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK='✔'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    status_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        print("Long Break")
        status_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)

    # If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        print("Break")
        status_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    # If it's the 1st/3rd/5th/7th rep:
    else:
        print("Work")
        status_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer
    count_in_minutes = math.floor(count / 60)
    count_in_seconds = count % 60

    if 9 >= count_in_minutes:
        count_in_minutes = f"0{count_in_minutes}"
    if 9 >= count_in_seconds:
        count_in_seconds = f"0{count_in_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_in_minutes}:{count_in_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            no_of_checkmarks = CHECK_MARK * math.floor(reps / 2)
            check_mark.config(text=no_of_checkmarks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Pal")
window.config(padx=100, pady=50, bg=YELLOW)

# This canvas is for the Tomato image with a size of 220 x 224
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png") # Read an image file to be added as arg in the canvas object
canvas.create_image(110, 112, image=tomato_png) # The width and height is half of the canvas so that my tomato will be hanging in the center of the canvas
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
start_button = Button(window, text="Start", fg=BLACK, font=(FONT_NAME, 9, "bold"), cursor="hand2", command=start_timer)
reset_button = Button(window, text="Reset",  fg=BLACK, font=(FONT_NAME, 9, "bold"), cursor="hand2", command=reset_timer)
status_label = Label(window, text="Timer",font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
check_mark = Label(window, fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)

# Set Custom Icon for Pomodoro App
window.wm_iconphoto(True, tomato_png)

# Grid Function for Layout
status_label.grid(row=0, column=1, sticky=N)
start_button.grid(row=2, column=0, sticky=S)
reset_button.grid(row=2, column=2, sticky=E)
check_mark.grid(row=3, column=1, sticky=S)
canvas.grid(row=1, column=1, sticky=N)


#canvas.pack() | Remove this pack() method, grid() will be used for layout because it's much easier

window.mainloop()
