# numbers = [1, 2, 3]

# new_list = [(n+1) for n in numbers]
# print(new_list)

# name = "Razee"
# list_name = [n for n in name]
# print(list_name)


# nums_list = [(2*x) for x in range(1,5)]
# print(nums_list)

new_names = ["Alex", "Razee", "Beth", "Abhilasha", "Dave", "Niggaman"]

short_names = [x.upper() for x in new_names if len(x) > 4]
print(short_names)