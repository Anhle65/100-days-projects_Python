import requests
import os
api_key = "69f04e4613056b159c2761a9d9e664d2"
# api_key = os.environ.get("api_key")
# This line is about the environment using to secure the password or api key from being hacked
# when public the code on website.
parameter = {
    "lat": -43.532055,
    "lon": 172.636230,
    "appid": api_key
}
website = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
data = website.json()['hourly']
time_rain = []
for status in data[:12]:
    if status['weather'][0]['id'] < 700:
        time_rain.append(status["rain"])
        condition = True
if condition == True:
    print("You should bring an umbrella along")
    print(time_rain)
