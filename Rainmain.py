import os
import requests
from twilio.rest import Client

import smtplib

# can set envioment vars in terminal
# e.g $env:TWILIO_ACCOUNT_SID="your_account_sid_here", list of env vars: dir ENV:

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "99456989e5d91540de91d1414e987388"  # unique api key, list of api's: apilist.fun

account_sid = "AC43e3abe8c73da8e413dd8883c373bc93"
auth_token = "1d2745bfae6bba9eb7b92404b5616a02"

weather_parameters = {
    "lat": 52.281940,
    "lon": -1.584470, #latlong.net
    "appid": api_key,
    "cnt": 4,    # only 1st 4 items in data
}

response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
#print(response.status_code)
weather_data = response.json()   # https://jsonviewer.stack.hu/
#weather_list = weather_data["list"]

will_rain = False
for weather_period in weather_data["list"]:
    weather_id = weather_period["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="Bring an umbrella",
    #     from_="+19478370432",
    #     to="+447710594086",
    # )
    # print(message.status)

    MY_EMAIL = "rav950py@gmail.com"
    PASSWORD = "ivfawzpnctkywkwb"

    with smtplib.SMTP("smtp.gmail.com") as connection: #smtp.mail.yahoo.com
        connection.starttls() # encrpt message
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
            msg="Subject:Weather Alert\n\nBring an umbrella")

#print(weather_data)
# print(data["list"][1]["weather"][0]["id"])  # list in dict, weather indice 1, 0 access inside list, id tag
# print(data["list"][1]["weather"][0]["description"])



