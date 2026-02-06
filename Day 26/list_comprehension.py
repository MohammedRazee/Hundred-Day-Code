# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]

# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [n for n in name]
# print(new_list)

# doubled_num = [n * 2 for n in range(1, 5)]
# print(doubled_num)


names = ["Alex", "Beth", "Charoline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
