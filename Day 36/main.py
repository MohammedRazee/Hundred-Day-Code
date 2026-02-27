import requests
from datetime import date, timedelta
import math
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "tesla+business"

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv("STOCK_KEY"),
}
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "language": "en",
    "pageSize": 3,
    "apiKey": os.getenv("NEWS_KEY")
}

STOCK_API = "https://www.alphavantage.co/query?"
NEWS_API = " https://newsapi.org/v2/everything?"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before = str(today - timedelta(days=2))

# stock = requests.get(url=STOCK_API, params=STOCK_PARAMS)
# stock.raise_for_status()
# stock_data = stock.json()["Time Series (Daily)"]

stock_data =  {
    "2026-02-26": {
        "1. open": "239.7100",
        "2. high": "247.4899",
        "3. low": "238.9500",
        "4. close": "242.0100",
        "5. volume": "7308059"
    },
    "2026-02-25": {
        "1. open": "233.2200",
        "2. high": "239.5500",
        "3. low": "231.2200",
        "4. close": "237.5400",
        "5. volume": "8569713"
    },
    "2026-02-24": {
        "1. open": "227.8000",
        "2. high": "236.5937",
        "3. low": "223.6300",
        "4. close": "229.3200",
        "5. volume": "13379817"
    },
}


yesterday_close = float(stock_data[yesterday]["4. close"])
before_close = float(stock_data[day_before]["4. close"])

per_close = before_close - yesterday_close
per_close = per_close / before_close * 100


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if per_close >= 5 or per_close <= -5:
    news = requests.get(url=NEWS_API, params=NEWS_PARAMS)
    news.raise_for_status()
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    news_data = news.json()["articles"]
    
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    for info in news_data:
        title = info["title"]
        desc = info["description"]
        if per_close >= 5:
            change = f"🔺{per_close}%"
        else:
            per_close *= -1
            change = f"🔻{per_close}%"

        client.api.account.messages.create(
            body=f"""TSLA: {change}
Headline: {title}
Brief: {desc}
""",
            from_="+13863462899",
            to="+919382036996",
        )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

