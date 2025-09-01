from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electrice", "Water", "Fire"])
table.add_column("Effective Against", ["Water", "Fire", "Earth"])
table.align = "l"

print(table)