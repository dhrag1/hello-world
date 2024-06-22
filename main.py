import requests
import json
from pprint import pprint


API_Key = "ac7d86d60ad244e90196bf7b85bb7cc4"

# Start
print("-----------------------------------------------------------------------------------------------------------------------")
print("Welcome to the Weather Report.")

while True:

    unit_type = input("For metric units, type 'm'. For U.S. customary units, type 'c'. Then press enter. ")

    if (unit_type.lower() != "m" and unit_type.lower() != "c"):
        print("Invlaid unit type.")

    else: 
        if unit_type.lower() == "m":
            unit = "Celsius"
        elif unit_type.lower() == "c":
            unit = "Fahrenheit"
        break

city = input("Enter a city name to see its current weather forecast: ")

# Call to API for current weather data
base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+API_Key

weather_data = requests.get(base_url).json()
# weather_data - Python dictionary (values for different weather components, such as temperature)
# to print all values in the weather_data dictionary, use pprint(weather_data)

temperature = float(weather_data["main"]["temp"])
feels_like = float(weather_data["main"]["feels_like"])
high_temp = float(weather_data["main"]["temp_max"])
low_temp = float(weather_data["main"]["temp_min"])
humidity = int(weather_data["main"]["humidity"])

if (unit_type == "m"):
    print("In " + weather_data["name"] + ", It is currently " + str(round(temperature - 273.15, 1)) + " degrees Celsius")
    print("It feels like " + str(round(feels_like - 273.15, 1)) + " degrees Celsius")
    print("The humidity level is " + str(humidity) + "% right now")
    print("-----------------------------------------------------------------------------------------------------------------------")

if (unit_type == "c"):
    print("In " + weather_data["name"] + ", It is currently " + str(round(1.8*(temperature - 273.15)+32, 1)) + " degrees Fahrenheit")
    print("It feels like " + str(round(1.8*(feels_like - 273.15)+32, 1)) + " degrees Fahrenheit")
    print("The humidity level is " + str(humidity) + "% right now")
    print("-----------------------------------------------------------------------------------------------------------------------")
