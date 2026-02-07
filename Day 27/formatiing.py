# pack(), place(), grid()

from tkinter import *

def button_clicked(user_input):
    my_label.config(text=user_input)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)     # Adding padding


# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"
my_label.config(text = "New Text", padx=50, pady=50)  # Same as above


# Button

button = Button(text="Click Me", command=lambda: button_clicked(input.get()))

# Entry
input = Entry(width=10)


# Pack Layout Manager

# my_label.pack(side="left")
# button.pack(side="left")
# input.pack(side="left")



# Place Layout manager

# my_label.place(x=100, y=200)
# button.place(x=0, y=0)
# input.place(x=0, y=0)


# Grid Layout manager (Best)

my_label.grid(row=0, column=0)
button.grid(row=1, column=1)
input.grid(row=2, column=3)

new_button = Button(text="New Button")
new_button.grid(row=0, column=2)




window.mainloop()
