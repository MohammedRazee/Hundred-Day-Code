from dotenv import load_dotenv
import os
import smtplib

load_dotenv()
my_email = os.getenv("SENDER")
get_email = os.getenv("RECEIVER")
pwd = os.getenv("PWD")


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=pwd)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=get_email, 
        msg="Subject:Hello\n\nThis is the body of my email")

