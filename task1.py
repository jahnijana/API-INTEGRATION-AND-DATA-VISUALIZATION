import json
import requests
import matplotlib.pyplot as plt

# API to fetch the temperature of a city
city_name = input('Enter a city name: ')
api_key = 'a34ba2e905d8676c0ffcb8ab6c2ceaea'

# To build the API URL
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

# Get server information
get_server_information = requests.get(api_url)
data = get_server_information.json()

# Check if the request was successful
if data['cod'] != 200:
    print(f"Error: {data.get('message', 'Unable to fetch data')}")
else:
    # Extracting necessary information
    city = data['name']
    country = data['sys']['country']
    temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
    feels_like = data['main']['feels_like'] - 273.15
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather_main = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description']

    # Display extracted data
    print(f"City: {city}, Country: {country}")
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Feels Like: {feels_like:.2f}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather: {weather_main} ({weather_desc})")

    # Visualizing the data
    labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Wind Speed (m/s)']
    values = [temperature, feels_like, humidity, wind_speed]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'green', 'orange', 'purple'])
    plt.title(f"Weather Data for {city}, {country}")
    plt.ylabel("Values")
    plt.tight_layout()
    plt.show()
