import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

SENDER_ADDR = os.getenv("SENDER")
RECEIVER_ADDR = os.getenv("RECEIVER")
PWD = os.getenv("PASSWORD")

MY_LAT = 12.971599 # Your latitude
MY_LONG = 77.594566 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS latitude: {iss_latitude}")
    print(f"ISS longitude: {iss_longitude}")

    if MY_LAT-5 <= iss_latitude >= MY_LAT+5 and MY_LONG-5 <= iss_longitude >= MY_LONG+5:
        return True
    
    return False

#Your position is within +5 or -5 degrees of the ISS position.

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

    time_now = datetime.now()
    hour = time_now.hour

    return hour <= sunrise and hour >= sunset


while True:
    time.sleep(60)
    
    if near_me() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=SENDER_ADDR, password=PWD)
            conn.sendmail(
                from_addr=SENDER_ADDR,
                to_addrs=RECEIVER_ADDR,
                msg="Subject:It's Sattelite Time \n\nLook up the ISS Station is passing by!"
            )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



