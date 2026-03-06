import os
from dotenv import load_dotenv
import requests
import pandas as pd
from flight_search import FlightSearch
load_dotenv()

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.api_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.HEADER = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('BEARER')}"
        }

    def get_sheet(self):
        response = requests.get(url=self.api_endpoint, headers=self.HEADER)
        response.raise_for_status()
        return response.json()
    
    def fill_iata(self, sheet_data):
        """Function used to fill in missing IATA code values in the Sheet."""
        data = sheet_data
        df = pd.DataFrame(data['prices'])
        df.replace('', pd.NA, inplace=True)

        if df["iataCode"].isna().any():
            missing_cols = df['iataCode'].isna()

            for idx in missing_cols.index:
                city_name = str(df.loc[idx, "city"])
                flight = FlightSearch()
                city_code = flight.get_city_iata(city_name=city_name)
                object_id = str(df.loc[idx, "id"])
                insert_json = {
                    "price": {
                        "iataCode": city_code,
                    }
                }
                
                insert_iata = requests.put(url=f"{self.api_endpoint}/{object_id}", json=insert_json, headers=self.HEADER)
                insert_iata.raise_for_status()
        
        return df.to_dict(orient="records")
