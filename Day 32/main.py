from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
my_email = "razeeismail15@gmail.com"
pwd = os.getenv("PWD")


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=pwd)
