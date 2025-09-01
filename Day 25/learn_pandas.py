import pandas as pd

data = pd.read_csv("data/weather_data.csv")
# print(type(data))
# print(data["temp"])


# data_dict = data.to_dict()


# temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get Column
# print(data["condition"])
# print(data.condition)


# Get Row
# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
temp = (monday.temp * 9/5) + 32
print(temp)


# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "razee"],
#     "scores": [76, 65, 89],
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("data/new_data.csv")
