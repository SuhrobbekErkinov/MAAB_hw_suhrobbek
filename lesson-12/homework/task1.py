from bs4 import BeautifulSoup


def parse_weather_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    weather_data = []
    rows = soup.find("tbody").find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text.strip()
        temperature = int(cols[1].text.strip().replace("°C", ""))
        condition = cols[2].text.strip()
        weather_data.append({"Day": day, "Temperature": temperature, "Condition": condition})

    return weather_data


def display_weather_data(weather_data):
    print("5-Day Weather Forecast:")
    for entry in weather_data:
        print(f"{entry['Day']}: {entry['Temperature']}°C, {entry['Condition']}")


def find_extreme_conditions(weather_data):
    highest_temp_day = max(weather_data, key=lambda x: x["Temperature"])
    sunny_days = [entry["Day"] for entry in weather_data if entry["Condition"] == "Sunny"]

    print(f"\nHottest Day: {highest_temp_day['Day']} with {highest_temp_day['Temperature']}°C")
    print(f"Sunny Days: {', '.join(sunny_days)}")


def calculate_average_temperature(weather_data):
    avg_temp = sum(entry["Temperature"] for entry in weather_data) / len(weather_data)
    print(f"\nAverage Temperature for the Week: {avg_temp:.2f}°C")


def main():
    file_path = "weather.html"
    weather_data = parse_weather_html(file_path)
    display_weather_data(weather_data)
    find_extreme_conditions(weather_data)
    calculate_average_temperature(weather_data)


if __name__ == "__main__":
    main()
