''' There is no Block Scope in Python!'''

# if 3 > 2:
#     a_variable = 10

# print(a_variable)


game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
