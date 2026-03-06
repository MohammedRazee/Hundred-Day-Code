import os
from dotenv import load_dotenv
import requests
load_dotenv()

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.api_key = os.getenv("AMA_KEY")
        self.api_secret = os.getenv("AMA_SECRET")
        self._token = self.get_new_token()
        self.header = {
            "accept": "application/vnd.amadeus+json",
            "Authorization": f"Bearer {self._token}"
        }

    def get_city_iata(self, city_name):
        """Get the IATA code of any city."""

        parameters = {
            "keyword": city_name,
            "max": 1
        }
        
        get_city_code = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", params=parameters, headers=self.header)
        get_city_code.raise_for_status()
        return get_city_code.json()["data"][0]["iataCode"]

    def get_new_token(self):
        self.get_json = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", data=self.get_json, headers={"content-type": "application/x-www-form-urlencoded"})
        response.raise_for_status()
        token = response.json()["access_token"]
        return token
    
    def check_flights(self, from_date, to_date, origin_code, destination_code):
        flight_check_headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_date,
            "returnDate": to_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=query, headers=flight_check_headers)
        if response.status_code != 200:
            print(f"check_flight() response error: {response.raise_for_status()}")
            return None
        return response.json()

