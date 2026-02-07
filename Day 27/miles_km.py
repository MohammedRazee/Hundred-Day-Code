from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# User input
input = Entry()

# Texts in the space

def convert_to_km(value):
    ans = round(int(value) * 1.609)
    output.config(text=ans)

miles = Label(text="Miles")
isqt = Label(text="is equal to")
km = Label(text="Km")
output = Label(text="0")

# Action Button
button = Button(text="Calculate", command=lambda: convert_to_km(input.get()))


# Placing entities

input.grid(row=0, column=2)
miles.grid(row=0, column=3)
isqt.grid(row=1, column=1)
output.grid(row=1, column=2)
km.grid(row=1, column=3)
button.grid(row=2, column=2)







window.mainloop()
