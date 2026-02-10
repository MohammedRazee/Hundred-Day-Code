from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_nums = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_nums
    shuffle(password_list)

    gen_password = "".join(password_list)
    pyperclip.copy(gen_password)

    pwd_in.delete(0, END)
    pwd_in.insert(END, gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save(web, user, password):
    website_in.delete(0, END)
    pwd_in.delete(0, END)

    new_data = {
        web: {
            "email": user,
            "password": password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields", message="Please don't leave any of the fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

# ---------------------------- Search Passwords ------------------------------- #

def show_details():
    web = website_in.get().capitalize()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            item = data[web]
            messagebox.showinfo(title=web, message=f"Email: {item['email']} \nPassword: {item['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="No Details Available", message=f"There are no details in the database")
    except KeyError:
        messagebox.showerror(title="No Details Available", message=f"There are no details for {web} in the database")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)


# Labels
website = Label(text="Website")
email = Label(text="Email/Username:")
pwd = Label(text="Password:")

# Entry fields
website_in = Entry(width=21)
website_in.focus()
email_in = Entry(width=45)
email_in.insert(END, "sample@example.com")
pwd_in = Entry(width=24)

# Buttons
gen_p = Button(text="Generate Password", width=21, highlightthickness=0, command=generate_password)
add = Button(text="Add", width=38, highlightthickness=0, command= lambda: save(website_in.get().capitalize(), email_in.get(), pwd_in.get()))
search = Button(text="Search", width=21, command=show_details)

# Placing UI
canvas.grid(row=0, column=1)

website.grid(row=1, column=0)
email.grid(row=2, column=0)
pwd.grid(row=3, column=0)

website_in.grid(row=1, column=1)
email_in.grid(row=2, column=1, columnspan=2)
pwd_in.grid(row=3, column=1)

gen_p.grid(row=3, column=2)
add.grid(row=4, column=1, columnspan=2)
search.grid(row=1, column=2)

window.mainloop()
