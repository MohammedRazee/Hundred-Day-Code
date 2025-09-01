import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""

for n in chosen_word:
    placeholder += "_"

print(placeholder)

result = "" 

while result != chosen_word:
    result = ""
    guess = input("\nGuess a letter: ").lower()
    for letter in chosen_word:
        if guess == letter:
            result += guess
        else:
            result += "_"
    print(result)

