import requests

aip_key = "50091b8c6a8923ad79620791472d4ac7"
URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 54.3150,
    "lon": 130.3208,
    "appid": aip_key,
    "exclude": "current,minutely,daily",

}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
data = response.json()

for i in range(12):
    if data["hourly"][i]["weather"][0]["id"] < 700:
        print("Bring your umbrella.")


