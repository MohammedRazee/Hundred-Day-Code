import os
from dotenv import load_dotenv
import requests
from datetime import datetime


WEIGHT = 90
HEIGHT = 165
AGE = 24
GENDER = "male"
load_dotenv()

BEARER = os.getenv("BEARER")

HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": os.getenv("API_ID"),
    "x-app-key": os.getenv("API_KEY")
}

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = "https://api.sheety.co/6c6ceb6fd2967fc13176875f3953d043/workouts,I'mNeverReallyDoingLmao/workouts"


data = {
    "query": "",
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}

query = input("Tell me about your workout today: ")
queries = query.split("and")
queries = [query.strip() for query in queries]

for query in queries:
    data["query"] = query

    response_nutrition = requests.post(url=nutrition_endpoint, json=data, headers=HEADERS)
    print(f"Response generated: {response_nutrition.status_code}")

    nutrition_data = response_nutrition.json()["exercises"][0]
    today = datetime.now()
    date = today.strftime('%x')
    time = today.strftime('%X')


    table_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": nutrition_data["name"],
            "duration": nutrition_data["duration_min"],
            "calories": nutrition_data["nf_calories"],
        }
    }
    header = {
        "Content-Type": "application/json",
        "Authorization": BEARER,
    }

    update_table = requests.post(url=sheety_endpoint, json=table_data, headers=header)
    print(f"Table Updated: {update_table.status_code}")


