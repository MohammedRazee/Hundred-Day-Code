import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.now()

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "19",
}

graph_edit = {
    "quantity": "13"
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
