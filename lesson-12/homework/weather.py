import requests
import os

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

city = input("Enter the name of the city: ")

url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"

locations = requests.get(url)

if locations.status_code!=200:
    print("Error occured")
    exit(0)

locations = locations.json()

if len(locations)==0:
    print("Not found, try again.")
    exit(0)

lat = locations[0]["lat"]
lon = locations[0]["lon"]

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

weather = requests.get(url).json()

def kelvin_to_celcius(temperature):
    return temperature - 273.15

print(f"The current weather in {locations[0]["name"]} is {kelvin_to_celcius(weather["main"]["temp"]) : .2f} °C")