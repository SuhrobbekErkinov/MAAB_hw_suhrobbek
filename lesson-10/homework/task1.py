import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "City": data["name"],
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"].capitalize()
        }
        return weather_info
    elif response.status_code == 401:
        return "Error: Invalid API key. Please check and update your API key."
    elif response.status_code == 404:
        return f"Error: City '{city}' not found."
    else:
        return f"Error: Unable to fetch data. Status code: {response.status_code}"

def main():
    city = "Tashkent"  # Change this to any city you want
    api_key = "1f571543451e47a2c1d9ccb89b1cfc0e"  # Replace with your OpenWeatherMap API key
    weather = get_weather(city, api_key)
    print(weather)

if __name__ == "__main__":
    main()
