print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

print("You are at a cross road. Where do you want to go?")
road = input("\tType \"left\" or \"right\"\n").lower()


#Smarter thing to do here is to convert everything to the lower case instead of putting or or over and over again

if road == "left":
    print('You\'ve come to a lake. '
          'There is an island in the middle of the lake.')
    island = input("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()

    if island == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("\tOne red, one yellow and one blue. Which colour do you choose?\n").lower()

        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "red":
            print("Burned by fire.\n MORTIS")
        elif door == "blue":
            print("Eaten by beasts.\n MORTIS")
        else:
            print("MORTIS")

    else:
        print("Attacked by fish which is an animal and you should be scared of it cause those two buffons were fighting abuot it. Iykyk\n MORTIS")

else:
    print("Fall into a hole.\n MORTIS")