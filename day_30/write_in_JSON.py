from tkinter import *
from tkinter import messagebox
import random
import json
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
    website_entry = website.get()
    password_entry = pass_enter.get()
    email = user.get()
    new_data = {
        website_entry: {
            'email': email,
            'password': password_entry,
            }
        }
    if website_entry == '' or password_entry == '':
        messagebox.showerror(title='ERROR', message="You haven't filled in all the information")
    else:
        check_pleased = messagebox.askokcancel(title=website_entry, message=f"These are the details you entered:\n"
                                                            f"Website: {website_entry}\nPassword: {password_entry}\n"
                                                            f"Is it OK to save?")
        if check_pleased:
            try:
                with open('password.json', 'r') as outfile:
                    data = json.load(outfile)
            # Open file if not exists and write into it
            except FileNotFoundError:
                with open('password.json', 'w') as outfile:
                    json.dump(new_data, outfile, indent=4)
            # If not error then updating the data to write
            else:
                data.update(new_data)
                with open('password.json', 'w') as outfile:
                    # print(data)
                    json.dump(data, outfile, indent=4)
            finally:
                website.delete(0, END)
                pass_enter.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search_password():
    """search password of the website"""
    name = website.get()
    try:
        with open("password.json", 'r') as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message="No Data File Found.")
    else:
        if name in data.keys():
            messagebox.showinfo(title="Your password", message=f"Website: \"{name}\"\n"
                                                                f"Email: {data[name]['email']}\nPassword: {data[name]['password']}")
        else:
            messagebox.showerror(title="Error found", message=f"No Data File of Website \"{name}\" Found.")


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
generate = Button(text="Generate Password", width=14, command=create_password)
generate.grid(row=3, column=2)
add = Button(text='Add', width=44, command=write_on_file)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", width=14, command=search_password)
search.grid(row=1, column=2)

# Entries
website = Entry(width=33)
website.grid(row=1, column=1)
website.focus()
user = Entry(width=52)
user.grid(row=2, column=1, columnspan=2)
user.insert(0, "levananh@gmail.com")
pass_enter = Entry(width=33)
pass_enter.grid(row=3, column=1)

window.mainloop()
