##################### Extra Hard Starting Project ######################

import datetime as dt
from dotenv import load_dotenv
import os
import pandas as pd
import random
import smtplib

load_dotenv()
SENDER = os.getenv("SENDER")
PWD = os.getenv("PWD")


def send_mail(name, email):
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        text = letter.read()
        text = text.replace("[NAME],", f"{name},")
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=SENDER, password=PWD)
        conn.sendmail(
            from_addr=SENDER,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{text}"
        )


data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict()

now = dt.datetime.now()
day = now.day
month = now.month

for _, people in data.iterrows():
    if people["month"] == month and people["day"] == day:
        send_mail(people["name"], people["email"])



