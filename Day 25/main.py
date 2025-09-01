# with open("data/weather_data.csv") as file:
#     data = file.readlines()
#     print(type(data))

import csv

with open ("data/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
