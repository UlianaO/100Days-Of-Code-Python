# The script checks if it will be rainining in Lutz withon the next 12 hours,
# and sends an SMS with Twilio if so.

import requests
import pprint as p
from twilio.rest import Client
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
# ---------------------- WEATHER  ---------------------- #
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("API_KEY")

weather_parameters = {
    "lat": 28.1511,
    "lon": -82.461479,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# ---------------------- SMS  ---------------------- #
twilio_phone_number = os.getenv("PHONE_NUM")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

response = requests.get(endpoint, params=weather_parameters)
response.raise_for_status()

weather_data = response.json()
weather_part = weather_data["hourly"][:12] # slices 12 hour in total

raining = False
for hour in weather_part:
    code = hour["weather"][0]["id"]
    if int(code) < 700:
        raining = True

if raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It`s raining today",
        from_=twilio_phone_number,
        to='+13462245944'
    )

    print(message.status)

