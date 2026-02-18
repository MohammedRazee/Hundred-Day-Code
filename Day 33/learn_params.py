import requests
from datetime import datetime

MY_LAT = 12.971599
MY_LNG = 77.594566
parameters = {
    "lat": MY_LAT,
    "lng":MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

timenow = datetime.now()
print(timenow.hour)
print(sunrise)
print(sunset)


