import pandas as pd

data = pd.read_csv("./data/weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["condition"].to_list()

# # print(type(data["temp"]))
# # print(data_dict)
# # print(temp_list)

# avg_temp = data["temp"].mean()
# print(avg_temp)
# print(data["temp"].max())

# # Getting data in Columns

# print(data["condition"])
# print(data.condition)


# # Getting data in Row

# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# temperature = monday.temp[0] * 1.8 + 32
# print(temperature)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data_new = pd.DataFrame(data_dict)
print(data_new)
data_new.to_csv("new_data.csv")
