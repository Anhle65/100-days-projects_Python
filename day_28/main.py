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
timer_clock = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer_clock)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer")
    reps = 0
    tick_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Long Break", fg='red')
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        label.config(text="Work Time", fg='blue')
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Short Break", fg='red')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minute = math.floor(count / 60)
    if minute < 10:
        minute = '0' + str(minute)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    if count >= 0:
        global timer_clock
        canvas.itemconfigure(timer, text=f'{minute}:{seconds}')
        timer_clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        number_tick = math.floor(reps / 2)
        tick_mark.config(text=f"{'✓'*number_tick}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50, bg=PINK)

label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 30, 'bold'), bg=PINK)
label.grid(row=0, column=1)

image_used = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
canvas.create_image(100, 112, image=image_used)
canvas.grid(row=1, column=1)
timer = canvas.create_text(100, 130, text="00:00", fill='orange', font=('center', 20, 'bold'))

tick_mark = Label(font=('center', 20, 'bold'), foreground=GREEN, background=PINK)
tick_mark.grid(row=3, column=1)

reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

window.mainloop()
