from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

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

    if len(web) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showerror(title="Empty Fields", message="Please don't leave any of the fields empty")
    else:
        isok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail:{user}"
                            f"\nPassword: {password} \nIs it ok to save?")
        
        if isok:
            with open("saved_passwords.txt", "a") as file:
                text = f"{web} | {user} | {password} \n"
                file.writelines(text)

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
website_in = Entry(width=45)
website_in.focus()
email_in = Entry(width=45)
email_in.insert(END, "sample@example.com")
pwd_in = Entry(width=26)

# Buttons
gen_p = Button(text="Generate Password", highlightthickness=0, command=generate_password)
add = Button(text="Add", width=38, highlightthickness=0, command= lambda: save(website_in.get(), email_in.get(), pwd_in.get()))

# Placing UI
canvas.grid(row=0, column=1)

website.grid(row=1, column=0)
email.grid(row=2, column=0)
pwd.grid(row=3, column=0)

website_in.grid(row=1, column=1, columnspan=2)
email_in.grid(row=2, column=1, columnspan=2)
pwd_in.grid(row=3, column=1)

gen_p.grid(row=3, column=2)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
