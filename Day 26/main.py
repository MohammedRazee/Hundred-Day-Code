import pandas as pd

df = pd.read_csv("data/nato_phonetic_alphabet.csv")
data = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Enter your name: ").upper()
alphabet_list = [n for n in name]

nato_phonetics = [data[n] for n in name]
print(nato_phonetics)

