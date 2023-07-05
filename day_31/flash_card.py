from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# window.minsize(80, 526)
# window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# canvas = Canvas(width=800, height=526)
# canvas.grid(row=0, column=0, columnspan=2)
def back_flash():

    canvas = Canvas(width=800, height=526)
    photo = PhotoImage(file='card_back.png', height=526, width=800)
    canvas.create_image(400, 263, image=photo)
    canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
    canvas.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
    canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))
    canvas.grid(row=0, column=0, columnspan=2)

def front_flash():

    canvas1 = Canvas(width=800, height=526)
    photo1 = PhotoImage(file='card_front.png', height=526, width=800)
    canvas1.create_image(400, 263, image=photo1)
    canvas1.config(highlightthickness=0, background=BACKGROUND_COLOR)
    canvas1.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
    canvas1.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))
    canvas1.grid(row=0, column=0, columnspan=2)
# window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# canvas = Canvas(width=800, height=526)
# photo = PhotoImage(file='card_back.png', height=526, width=800)
# canvas.create_image(400, 263, image=photo)
# canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
# canvas.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
# canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))
# canvas.grid(row=0, column=0, columnspan=2)

# window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# canvas = Canvas(width=800, height=526)
# photo1 = PhotoImage(file='card_front.png', height=526, width=800)
# canvas.create_image(400, 263, image=photo1)
# canvas.config(highlightthickness=0, background=BACKGROUND_COLOR)
# canvas.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
# canvas.create_text(400, 263, text='trouve', font=('Ariel', 60, 'bold'))
# canvas.grid(row=0, column=0, columnspan=2)

tick = PhotoImage(file='right.png')
button = Button(image=tick, background=BACKGROUND_COLOR, highlightthickness=0, command=back_flash)
button.grid(row=1, column=1)
cross = PhotoImage(file='wrong.png')
button1 = Button(image=cross, highlightthickness=0, command=front_flash)
button1.grid(row=1, column=0)



# language = Label(highlightthickness=0, background=BACKGROUND_COLOR)
# language.config(text='English', font=('Ariel', 40, 'italic'))
# language.place(x=400, y=150)
# word = Label()
# word.config(text='trouve', font=("Ariel", 60, 'bold'))
# word.place(x=400, y=263)
window.mainloop()
