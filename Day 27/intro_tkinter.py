from tkinter import *

def button_clicked(user_input):
    my_label.config(text=user_input)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New text"
my_label.config(text = "New Text")  # Same as above

# Button

button = Button(text="Click Me", command=lambda: button_clicked(input.get()))
button.pack()

# Entry
input = Entry(width=10)
input.pack()








window.mainloop()
