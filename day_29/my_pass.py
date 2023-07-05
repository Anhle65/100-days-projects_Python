from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    """create a very strong password"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    pass_enter.delete(0, END)
    letter = [random.choice(letters) for i in range(nr_letters)]
    symbol = [random.choice(symbols) for i in range(nr_symbols)]
    number = [random.choice(numbers) for i in range(nr_numbers)]
    password_list = letter + symbol + number
    random.shuffle(password_list)
    pass_enter.insert(0, ''.join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_on_file():
    """write all the inputs in a file"""
    if website.get() == '' or pass_enter.get() == '':
        messagebox.showerror(title='ERROR', message="You haven't filled in all the information")
    else:
        check_pleased = messagebox.askokcancel(title=website.get(), message=f"These are the details you entered:\n"
                                                            f"Website: {website.get()}\nPassword: {pass_enter.get()}\n"
                                                            f"Is it OK to save?")
        if check_pleased:
            outfile = open('password.txt', 'a')
            outfile.write(f"{website.get()} | {user.get()} | {pass_enter.get()} \n")
            website.delete(0, END)
            pass_enter.delete(0, END)
            outfile.close()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Labels
web_name = Label()
web_name.config(text='Website:')
web_name.grid(row=1, column=0)
user_name = Label()
user_name.config(text="Email/Username:")
user_name.grid(row=2, column=0)
pass_word = Label()
pass_word.config(text="Password:")
pass_word.grid(row=3, column=0)

# Buttons
generate = Button(text="Generate Password", command=create_password)
generate.grid(row=3, column=2)
add = Button(text='Add', width=44, command=write_on_file)
add.grid(row=4, column=1, columnspan=2)

# Entries
website = Entry(width=52)
website.grid(row=1, column=1, columnspan=2)
website.focus()
user = Entry(width=52)
user.grid(row=2, column=1, columnspan=2)
user.insert(0, "levananh@gmail.com")
pass_enter = Entry(width=33)
pass_enter.grid(row=3, column=1)

window.mainloop()
