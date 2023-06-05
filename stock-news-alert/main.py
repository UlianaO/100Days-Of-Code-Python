# The script compares stock price between yesterday
# and the day before yesterday, sending me an SMS alerting whether
# the price went up or down, and sending 3 news articles related to the price change.

import requests
import os
from dotenv import load_dotenv
import json
import pprint as p
import datetime as dt
from twilio.rest import Client

load_dotenv()

STOCK = "SPY"
COMPANY_NAME = "S&P 500 ETF"
STOCK_SOURCE = "https://www.alphavantage.co/query"
API_KEY = os.getenv("STOCK_API_KEY")

NEWS_SOURCE = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

twilio_phone_number = os.getenv("PHONE_NUM")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
my_num = os.getenv("MY_NUM")

# https://www.alphavantage.co/documentation/ - > Daily Adjusted
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
# ------------------------ STOCK API --------------------------#

response = requests.get(STOCK_SOURCE, params=stock_parameters)

# API does not update on weekends.
# DateTime weekday() fn returns 0-6 for Monday-Sunday.
today = dt.datetime.now()
print(today.weekday())

if today.weekday() == 5 or today.weekday() == 6:
    exit()

# Time Series (Daily) --> 2023-05-31 --> close
if today.weekday() == 0: # on monday, look thursday-friday
    yesterday_date = str(dt.date.today() - dt.timedelta(days=3))
    two_days_ago = str(dt.date.today() - dt.timedelta(days=4))
elif today.weekday() == 1: # on tuesday, look friday-monday
    yesterday_date = str(dt.date.today() - dt.timedelta(days=1))
    two_days_ago = str(dt.date.today() - dt.timedelta(days=4))
else:
    yesterday_date = str(dt.date.today() - dt.timedelta(days=1))
    two_days_ago = str(dt.date.today() - dt.timedelta(days=2))

yesterday_close_price = response.json()["Time Series (Daily)"][yesterday_date]["4. close"]
two_days_ago_close_price = response.json()["Time Series (Daily)"][two_days_ago]["4. close"]

print(yesterday_close_price, two_days_ago_close_price)
p.pprint(response.json())
# Find the difference in stock prices
difference = float(yesterday_close_price) - float(two_days_ago_close_price)
difference_percent = difference / float(yesterday_close_price)*100

emoji = None

# ------------------------ NEWS API --------------------------#

if abs(difference_percent) > 0:
    # If the difference is negative, the price went down.
    if difference > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"

   # print(two_days_ago_close_price, yesterday_close_price, difference, emoji)
    news_response = requests.get(NEWS_SOURCE, params=news_parameters)
    # only three first articles needed
    all_articles = news_response.json()["articles"]
    articles = all_articles[:3]


# ------------------------ SMS MANAGER --------------------------#
    
    ############# MAKE IT SEND ALL 3 ARTICLES IN 1 SMS with LINKS
    formatted_articles = [f"{COMPANY_NAME}:{emoji} \n Title: {article['title']}.\n Description: {article['description']}"
                          for article in articles]
    client = Client(account_sid, auth_token)

    #Send each article via Twilio
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=twilio_phone_number,
            to=my_num
        )


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""