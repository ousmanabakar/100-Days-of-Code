import requests
MY_LAT = 41.0082
MY_LONG = 28.9784

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0:2]
sunset = data['results']['sunset'].split("T")[1].split(":")[0:2]
print(sunset)
print(sunrise)
