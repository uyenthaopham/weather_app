import requests

def get_weather(city):
    API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
