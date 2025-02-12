# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY:CODTECH IT SOLUTIONS

NAME:JANA JAHNI

INTERN ID:CT08PMC

DOMAIN:PYTHON PROGRAMMING

DURATION:25TH JAN 2025 TO 25TH FEB 2025

MENTOR:NEELA SANTHOSH


# Description:

I have done my first task of my internship on "API INTEGRATION AND DATA VISUALISATION" using python.I used the openweathermap website to fetch the temperature of a city and api url. The main steps I performed in this task is Fetching the data from the API,Process the API data for Visualisation and then Visualise the processed data and we obtain a visualised output.This code fetches and displays the current weather information of a city entered by the user. It uses the OpenWeatherMap API to retrieve the data, then processes and visualizes the information in a bar chart.

# Steps in the Code:

1. Import necessary libraries:
   - "json": Used to parse the JSON response from the API.
   - "requests": To send an HTTP request to the OpenWeatherMap API.
   - "matplotlib.pyplot": For plotting the weather data on a bar chart.

2. Get user input:
   - The user is prompted to enter a city name.

3. Build the API URL:
   - The API URL is constructed using the city name and a personal API key (which should be kept private).
   - Example URL format: `https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}`

4. Make the API request:
   - A GET request is sent to the OpenWeatherMap API to fetch weather data.
   - The JSON response from the API is parsed using `.json()`.

5. Check the request status:
   - If the request is unsuccessful (`data['cod'] != 200`), an error message is displayed.
   - If successful, the weather data is extracted:
     - `city` and `country` from `data['name']` and `data['sys']['country']`.
     - `temperature`, `feels_like`, `humidity`, `wind_speed`, and weather descriptions from the respective fields in the response.
   - The temperature is converted from Kelvin to Celsius using the formula `temp - 273.15`.

6. Display the extracted data:
   - The extracted weather data is displayed in the console.

7. Visualize the data:
   - A bar chart is created to visualize the following weather parameters:
     - Temperature (°C)
     - Feels Like (°C)
     - Humidity (%)
     - Wind Speed (m/s)
   - Different colors are used for each bar for distinction.
   - The chart is titled with the city and country name and labels are adjusted for clarity.

8. Show the plot:
   - The `plt.show()` function renders the bar chart on the screen.

# Output:

Console Output (assuming the user enters "New York"):


Enter a city name: New York
City: New York, Country: US
Temperature: -0.59°C
Feels Like: -5.09°C
Humidity: 93%
Wind Speed: 4.12 m/s
Weather: snow(snow)


# Bar Chart Output:

![Image](https://github.com/user-attachments/assets/1be246af-9f61-40dc-befe-4e83489d365e)

The chart will have the following labels with corresponding values on the y-axis:
- **Temperature (°C)**: -0.59
- **Feels Like (°C)**: -5.09
- **Humidity (%)**: 93
- **Wind Speed (m/s)**: 4.12

Each of these values will be represented by bars of different colors (blue, green, orange, purple) on the bar chart.








