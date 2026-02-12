import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("SENDER")
get_email = os.getenv("RECEIVER")
pwd = os.getenv("PWD")

now = dt.datetime.now()
day = now.weekday()

if day == 4:
    with open("quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=get_email, 
            msg=f"Subject:Monday Motivation\n\n{quote}")



