import requests
import smtplib as sm
import os

SENDER_EMAIL = os.environ.get("MY_SPAM_EMAIL")
SENDER_PASSWORD = os.environ.get("MY_SPAM_PASSWORD")
RECIEVER = os.environ.get("RECIEVER")
MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")
WEATHER_APPID = os.environ.get("APPIDWEATHER")
MESSAGE = "Subject:It finna rain today\n\nLmao"

parameters = {
    "lat":MY_LAT ,
    "lon":MY_LONG,
    "appid":WEATHER_APPID,
    "cnt": 8
}

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=OWM_endpoint,params=parameters)
response.raise_for_status()
data = response.json()["list"]
weather_ids = [item['weather'][0]['id'] for item in data]
print(weather_ids)
def grab_unbrealla(numbers: list):
    return any(num<700 for num in numbers)

if grab_unbrealla(weather_ids):
    with sm.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIEVER,
            msg=MESSAGE
        )
