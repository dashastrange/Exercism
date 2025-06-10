import requests

def get_current_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        city = data['name']
        country = data['sys']['country']
        result = (
            f"Current weather in {city}, {country}:\n"
            f"  Weather: {weather}\n"
            f"  Temperature: {temp}°C (feels like {feels_like}°C)\n"
            f"  Humidity: {humidity}%\n"
            f"  Wind speed: {wind_speed} m/s"
        )
        return result
    elif response.status_code == 404:
        return "City not found. Please check the city name."
    else:
        return f"Error: Unable to retrieve weather data (status code {response.status_code})."

# Usage example:
API_KEY = "YOUR_API_KEY_HERE"  # Replace with OpenWeatherMap API key
city = input("Enter city name: ")
print(get_current_weather(city, API_KEY))