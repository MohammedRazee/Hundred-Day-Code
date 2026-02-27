import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
today = datetime.now()

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN
}


graph_config = {
    "quantity": "13",
}


# response = requests.put(url=update_endpoint, json=graph_config, headers=headers)
response = requests.delete(url=update_endpoint, headers=headers)

print(response.text)
