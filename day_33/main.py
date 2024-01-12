import requests

MY_LAT = 6.524379
MY_LONG = 3.379206

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sun_data = (sunrise, sunset)
print(sun_data)