import pandas as pd
import numpy as np

data = pd.read_csv("./data/squirrel_data.csv")

fur_color = []
counts = []

for row in data.groupby("Primary Fur Color"):
    fur_color.append(row[0])

for x in fur_color:
    item = data[data["Primary Fur Color"] == x]
    counts.append(len(item))

data_dict = {
    "Fur Color": fur_color,
    "Count": counts,
}

df = pd.DataFrame(data=data_dict)
df.to_csv("squirrel_count.csv")


