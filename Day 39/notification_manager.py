import os
from dotenv import load_dotenv
from twilio.rest import Client
from flight_data import FlightData
load_dotenv()


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.api_sid = os.getenv("TWILIO_SID")
        self.api_token = os.getenv("TWILIO_AUTH")
    
    def send_notification(self, flight_data: FlightData):
        client = Client(self.api_sid, self.api_token)
        msg = f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_airport} to {flight_data.destination_airport}, on {flight_data.out_date} until {flight_data.return_date}."

        message = client.api.messages.create(
            body=msg,
            from_="+13863462899",
            to="+919382036996",
        )


        
    