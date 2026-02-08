from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps > 8:
        reset_timer()
    elif reps == 8:
        # count_down(long_break)
        title.config(text="Break", fg=RED)
        count_down(7)
    elif reps % 2 != 0:
        # count_down(work_sec)
        title.config(text="Work", fg=GREEN)
        count_down(5)
    else:
        # count_down(short_break)
        title.config(text="Break", fg=PINK)
        count_down(6)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


# Heading
title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))

# Start and Reset Buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

# Checkmark
check_mark = Label(fg=GREEN, bg=YELLOW,)

# Placing items
title.grid(row=1, column=2)
canvas.grid(row=2, column=2)
start.grid(row=3, column=1)
reset.grid(row=3, column=3)
check_mark.grid(row=4, column=2)



window.mainloop()
