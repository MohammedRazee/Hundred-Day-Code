import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""

for n in chosen_word:
    placeholder += "_"

print(placeholder)

corrected_letters = []
result = "" 

while result != chosen_word:
    result = ""
    guess = input("\nGuess a letter: ").lower()
    for letter in chosen_word:
        if guess == letter:
            result += guess
            if letter not in corrected_letters:
                corrected_letters.append(guess)
        elif letter in corrected_letters:
            result += letter
        else:
            result += "_"
    print(result)

if result == chosen_word:
    print("\n\nYou win!")
else:
    print("\n\nNo more guesses you lose")
