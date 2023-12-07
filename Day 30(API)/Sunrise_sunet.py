import requests

HOME_LAT = 28.28
HOME_LNG = 83.9960

parameters = {"lat": HOME_LAT, "lng": HOME_LNG, "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]

sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

result = f"Sunrise: {sunrise} AM\nSunset: {sunset} PM"

print(result)
