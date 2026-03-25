import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CACHE_EXPIRY_SECONDS = 600  # 10 minutes


# Format: { "city_name": (data_dict, timestamp) }
weather_cache = {}

def get_weather_data(city):
    """
    Fetches weather data from OpenWeather API with Caching and Error Handling.
    Returns: (data, error_message)
    """
    current_time = time.time()
    city = city.lower().strip()

    # 1. Check Cache first (Performance Optimization)
    if city in weather_cache:
        cached_data, timestamp = weather_cache[city]
        if current_time - timestamp < CACHE_EXPIRY_SECONDS:
            print(f"DEBUG: Returning cached data for {city}")
            return cached_data, None

    # 2. API Call (If not in cache or expired)
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        # Timeout set to 5 seconds to prevent the server from hanging
        response = requests.get(BASE_URL, params=params, timeout=5)
        
        # Raise an exception for 4xx or 5xx status codes
        response.raise_for_status()
        
        data = response.json()

        # 3. Data Transformation (Extracting only what we need)
        processed_data = {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"].capitalize(),
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "city": data["name"],
            "country": data["sys"]["country"]
        }

        # 4. Save to Cache
        weather_cache[city] = (processed_data, current_time)
        return processed_data, None

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return None, "City not found. Please check the spelling."
        return None, f"HTTP error occurred: {http_err}"
    
    except requests.exceptions.ConnectionError:
        return None, "Network error. Please check your internet connection."
    
    except requests.exceptions.Timeout:
        return None, "The request timed out. Please try again later."
    
    except Exception as err:
        return None, f"An unexpected error occurred: {err}"