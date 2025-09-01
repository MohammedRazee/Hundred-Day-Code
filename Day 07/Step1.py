import random

word_list = ["aardvark", "baboon", "camel"]

question = random.choice(word_list)
char = str(input("Guess a letter: ")).lower()

for n in question:
    if char == n:
        print("Right")
    else:
        print("Wrong")

print(f"The word was {question}")
