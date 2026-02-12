BACKGROUND_COLOR = "#B1DDC6"
FR_CARD = "./images/card_back.png"
ENG_CARD = "./images/card_front.png"

from tkinter import *
import pandas as pd
from random import choice

known_words = []

# ----------------------------------------------------------- READ CSV ------------------------------------------------------------ #

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")

french = data["French"]
fr_word = ""

def flip_card(eng_word, fr_word):
    card.config(file=ENG_CARD)
    flash.itemconfig(flash_img, image=card)
    flash.itemconfig(flash_lang, text="English", fill="black")
    flash.itemconfig(flash_word, text=eng_word, fill="black")

    # Buttons would have saved a lot of headache here
    yes.bind('<Button-1>', lambda event: we_know(fr_word, eng_word))
    no.bind('<Button-1>', start_game)

def start_game(event=None):
    fr_word = french.sample(n=1).iloc[0]
    eng_word = data.loc[data["French"] == fr_word, "English"].iloc[0]

    card.config(file=FR_CARD)
    flash.itemconfig(flash_img, image=card)
    flash.itemconfig(flash_lang, text="French", fill="white")
    flash.itemconfig(flash_word, text=fr_word, fill="white")

    flash.after(3000, flip_card, eng_word, fr_word)

def we_know(fr_word, eng_word, event=None):
    known_words.append(fr_word)
    french.drop(data[data["French"] == fr_word].index, inplace=True)
    start_game()

# ----------------------------------------------------------- BUILD UI ------------------------------------------------------------ #

window = Tk()
# window.minsize(width=800, height=526)
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# Canvases
flash = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
yes = Canvas(width=100, height=100, highlightthickness=0)
no = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)

# Placing Images into the canvases
flash_img = flash.create_image(400, 263, image=card)
flash_lang = flash.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="white")
flash_word = flash.create_text(400, 263, text=fr_word, font=("Ariel", 60, "bold"), fill="white")

start_game()

# ----------------- Buttons Can be images ------------------------ #

yes.create_image(50, 50, image=right_img)
no.create_image(50, 50, image=wrong_img)


# Placing UI
flash.grid(row=0, column=0, columnspan=2)
no.grid(row=1, column=0)
yes.grid(row=1, column=1)


window.mainloop()

for word in known_words:
    data.drop(data[data["French"] == word].index, inplace=True)

data.to_csv("./data/words_to_learn.csv", index=False)
    

