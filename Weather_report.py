import requests
import csv

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY = "1d3dc037b03d349d535d65cd283683b0"  
CITIES = [
    "Karachi", "Lahore", "Islamabad",
    "Quetta", "Peshawar", "Faisalabad",
    "Multan", "Sialkot", "Hyderabad"
]
CSV_FILE = "weather.csv"

# -----------------------------
# FETCH WEATHER DATA FUNCTION
# -----------------------------
def fetch_weather(city):
    """Fetch current weather data for a city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1d3dc037b03d349d535d65cd283683b0&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": city,
            "Temperature": data["main"]["temp"],
            "Feels Like": data["main"]["feels_like"],
            "Humidity": data["main"]["humidity"],
            "Description": data["weather"][0]["description"]
        }
    else:
        print(f" Failed to fetch data for {city}")
        return None

# -----------------------------
# SAVE TO CSV
# -----------------------------
def save_to_csv(weather_data):
    """Save list of weather dictionaries to CSV."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["City", "Temperature", "Feels Like", "Humidity", "Description"])
        writer.writeheader()
        for row in weather_data:
            writer.writerow(row)

# -----------------------------
# FIND HOTTEST & COLDEST CITIES
# -----------------------------
def analyze_weather():
    """Read CSV and find hottest & coldest cities."""
    hottest = None
    coldest = None

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp = float(row["Temperature"])
            if hottest is None or temp > hottest[1]:
                hottest = (row["City"], temp)
            if coldest is None or temp < coldest[1]:
                coldest = (row["City"], temp)

    print(f" Hottest City: {hottest[0]} ({hottest[1]}°C)")
    print(f" Coldest City: {coldest[0]} ({coldest[1]}°C)")

# -----------------------------
# MAIN PROGRAM
# -----------------------------
def generate_weather_report():
    weather_data = []
    for city in CITIES:
        print(f"Fetching weather for {city}...")
        data = fetch_weather(city)
        if data:
            weather_data.append(data)

    if weather_data:
        save_to_csv(weather_data)
        print(f"\n Weather data saved to {CSV_FILE}")
        analyze_weather()

# Run the program
if __name__ == "__main__":
    generate_weather_report()
