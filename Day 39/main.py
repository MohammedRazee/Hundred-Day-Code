#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import find_cheapest_flights
from flight_search import FlightSearch
from data_manager import DataManager
from datetime import date, timedelta
from notification_manager import NotificationManager
import time

ORIGIN_CITY_IATA = "LON"

sheety_mang = DataManager()
sheet_data = sheety_mang.get_sheet()
sheet_data = sheety_mang.fill_iata(sheet_data)

from_date = date.today() + timedelta(days=1)
to_date = from_date + timedelta(days=180)

for data in sheet_data:
    print(f"Getting flights for {data['city']}... ")
    dest_code = data["iataCode"]
    flights_ob = FlightSearch()
    flights = flights_ob.check_flights(from_date, to_date, ORIGIN_CITY_IATA, dest_code)
    cheap_flight = find_cheapest_flights(flights)
    print(f"{data['city']}: £{cheap_flight.price}")
    if cheap_flight.price != "N/A" and int(cheap_flight.price) < data["lowestPrice"]:
        notify = NotificationManager()
        notify.send_notification(cheap_flight)

    time.sleep(2)



